import pickle
PREFIX = {
    'บจ.': 'บริษัท',
    'บมจ.': 'บริษัท',
    'หจก.': 'ห้างหุ้นส่วนจำกัด',
    'หสน.': 'ห้างหุ้นส่วนสามัญนิติบุคคล',
    'หส.': 'ห้างหุ้นส่วนสามัญ',
    'อบต.': 'องค์การบริหารส่วนตำบล'
}

SUFFIX = {
    'บจ.': 'จำกัด',
    'บมจ.': 'จำกัด (มหาชน)'
}

if __name__ == "__main__":
    with open('dict/PREFIX.dictionary', 'wb') as dictionary_file:
        pickle.dump(PREFIX, dictionary_file)

    with open('dict/SUFFIX.dictionary', 'wb') as dictionary_file:
        pickle.dump(SUFFIX, dictionary_file)
