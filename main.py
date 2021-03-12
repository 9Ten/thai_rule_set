# To import libraries
from fastapi import FastAPI, Body, File, UploadFile, HTTPException
from typing import List
from pydantic import BaseModel

from trs.name import Name
from collections import Counter
from pythainlp.tag.named_entity import ThaiNameTagger
from pythainlp.util import countthai
from pythainlp.util import normalize
import string
import re
import pickle
import numpy as np
import pandas as pd
import io


# To import libraries for parallel processing
from dask.distributed import Client
import dask.dataframe as dd
import dask.bag as db
from dask import delayed
import multiprocessing
num_processes = multiprocessing.cpu_count()
client = Client(
    processes=False,
    threads_per_worker=4,
    n_workers=num_processes,
    memory_limit='2GB'
)


base_url = '/api/0.1'
description = """
A REST API for data discovery and data refinery in Thai
"""
app_config = {
    'title': 'DataToolsAPI',
    'description': description,
    'version': '0.1'
}
app = FastAPI(**app_config)
ner = ThaiNameTagger()

class Text(BaseModel):
    text: str


class TextList(BaseModel):
    text_list: list


''' Data Discovery + Classification Tools [Pythainlp] '''
def discovery(text: str, is_file: bool=False) -> dict:
    '''Find Named Entity Recognition
        DATE, TIME, EMAIL, LEN, LOCATION, ORGANIZATION, 
        PERSON, PHONE, URL, ZIP, Money, LAW
        https://www.thainlp.org/pythainlp/docs/2.0/api/tag.html
    '''
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    cleaned_text = normalize(regex.sub('', text))
    percent_thai = float(countthai(cleaned_text))
    result_ner = ner.get_ner(cleaned_text, pos=False)
    result_ner_counter = Counter([re.sub(r'B-|I-', '', word_ner_pair[1]) for word_ner_pair in result_ner])
    total_count_ner = sum([ner_counter[1] for ner_counter in result_ner_counter.most_common()])
    if is_file:
        result_dict = {
            "percent_thai": percent_thai,
            "total_count_ner": total_count_ner,
            "result_ner_counter": result_ner_counter
        }
    else:
        result_ner_dict = [{"ner_key": ner_counter[0], "ner_percent": round((ner_counter[1]/total_count_ner)*100.0, 2)}\
            for ner_counter in result_ner_counter.most_common()]
        result_dict = {
            "cleaned_text": cleaned_text,
            "percent_thai": percent_thai,
            "result_ner": result_ner_dict
        }
    return result_dict

def aggregate_ner_counter(ddf: dd, column_name: str) -> dict:
    result_ner_counter = Counter()
    percent_thai = []
    total_count_ner = 0
    for row in ddf:
        result_ner_counter += row["result_ner_counter"]
        percent_thai.append(row["percent_thai"])
        total_count_ner += row["total_count_ner"]
    result_ner_dict = [{"ner_key": ner_counter[0], "ner_percent": round((ner_counter[1]/total_count_ner)*100.0, 2)} for ner_counter in result_ner_counter.most_common()]
    result_dict = {"column_name": column_name, "percent_thai": round(np.mean(percent_thai), 2), "result_ner": result_ner_dict}
    return result_dict

# To refine by row
@app.post(base_url + "/data_discovery/text")
async def data_discovery_text(req_body: Text):
    result_dict = discovery(req_body.text)
    return {"result": result_dict}

# To refine by column
@app.post(base_url + "/data_discovery/text_list")
async def data_discovery_text_list(req_body: TextList):
    result_dict = db.from_sequence(req_body.text_list)\
        .map(lambda text: discovery(str(text)))\
        .compute()  # .compute(scheduler='processes')
    return {"result": result_dict}

# To refine by table
@app.post(base_url + "/data_discovery/text_file")
async def data_discovery_text_file(file: bytes = File(...)):
    ''' urlpath: string or list '''
    text_stream = io.BytesIO(file)
    df = pd.read_csv(text_stream, encoding='utf-8', dtype=str)
    column_list = df.columns.to_list()

    # To parallel processing with Dask
    ddf = dd.from_pandas(df, npartitions=4)\
        .map_partitions(lambda df: df.applymap(lambda text: discovery(text, True)))\
        .compute()  # .compute(scheduler='processes')

    # To aggregate result_ner_counter by column
    result_dict = db.from_sequence([(ddf[column], column) for column in column_list])\
        .map(lambda ddf_column: aggregate_ner_counter(ddf_column[0], ddf_column[1]))\
        .compute()  # .compute(scheduler='processes')
    return {"result": {"column_list": column_list, "result": result_dict}}


''' Data Refinery Tools '''
# To refine by row
@app.post(base_url + "/data_refinery/text")
async def data_refinery_text(req_body: Text):
    result_dict = Name(req_body.text)
    return {"result": result_dict}

# To refine by column
@app.post(base_url + "/data_refinery/text_list")
async def data_refinery_text_list(req_body: TextList):
    result_dict = db.from_sequence(req_body.text_list)\
        .map(lambda text: Name(str(text)))\
        .compute()  # .compute(scheduler='processes')
    return {"result": result_dict}

# To refine by table
@app.post(base_url + "/data_refinery/text_file")
async def data_refinery_text_file(file: bytes = File(...)):
    '''urlpath: string or list return json response'''
    text_stream = io.BytesIO(file)
    df = pd.read_csv(text_stream, encoding='utf-8', dtype=str)
    column_list = df.columns.to_list()

    # To parallel processing with Dask
    ddf = dd.from_pandas(df, npartitions=4)\
        .map_partitions(lambda df: df.applymap(lambda text: {'result': Name(text)}))\
        .compute()  # .compute(scheduler='processes')
    result_dict = [{"column_name": column, "output": ddf[column].to_list()}\
        for column in column_list]
    return {"result": {"column_list": column_list, "result": result_dict}}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, debug=True)
    # uvicorn main:app --reload
    # Limitation: 1000 rows
