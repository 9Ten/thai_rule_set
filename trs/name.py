import re
import pickle
from toolz import memoize


# collection_dict = LoadDictionary()
# To initial load collection of dictionary
# @memoize
# def LoadDictionary():
#     with open('../dict/IND_FULL_TO_ABBR_TITLE_CONVERT.dictionary', 'rb') as dictionary_file:
#         dictionary = pickle.load(dictionary_file)
#     with open('../dict/IND_ABBR_TO_FULL_TITLE_CONVERT.dictionary', 'rb') as index_dictionary_file:
#         abbr_dictionary = pickle.load(index_dictionary_file)
#     with open('../dict/IND_FULL_TITLE_TO_INDEX_CONVERT.dictionary', 'rb') as index_dictionary_file:
#         index_dictionary = pickle.load(index_dictionary_file)
#     with open('../dict/ORG_FULL_TO_ABBR_TITLE_CONVERT.dictionary', 'rb') as dictionary_file:
#         org_dictionary = pickle.load(dictionary_file)
#     with open('../dict/PREFIX.dictionary', 'rb') as dictionary_file:
#         prefix = pickle.load(dictionary_file)
#     with open('../dict/SUFFIX.dictionary', 'rb') as dictionary_file:
#         suffix = pickle.load(dictionary_file)
#     return dictionary, abbr_dictionary, index_dictionary, org_dictionary, prefix, suffix


# return {
#     'dictionary': dictionary,
#     'abbr_dictionary': abbr_dictionary,
#     'index_dictionary': index_dictionary,
#     'org_dictionary': org_dictionary,
#     'prefix': prefix,
#     'suffix': suffix
# }
# dictionary, abbr_dictionary, index_dictionary, org_dictionary, prefix, suffix = LoadDictionary()

def SetUnhandle():
    return 'UNHANDLE'


def RemoveSpecialChar(p, flag=True):
    if flag:
        p = re.sub('[^ก-๛A-Za-z0-9(). ]+', '', p)
    else:
        return p
    return p


def RemoveEmptyBracket(p):
    p = re.sub('\(\\s{0,}\)', '', p)
    p = re.sub('\({2,}', '', p)
    p = re.sub('\){2,}', '', p)
    p = re.sub('\)\\s{0,}\)', '', p)
    p = re.sub('\(\\s{0,}\(', '', p)
    p = re.sub('\(\\s{0,}\)', '', p)
    p = re.sub('\({2,}', '', p)
    p = re.sub('\){2,}', '', p)
    p = re.sub('\)\\s{0,}\)', '', p)
    p = re.sub('\(\\s{0,}\(', '', p)
    return p


def RemoveMultipleDot(p):
    p = re.sub('\.{2,}', '', p)
    return p


def ConcatIndividualTitle(TITLE):

    TITLE = TITLE.strip()
    index = 0
    isFound = True
    AT = ''
    FT = ''
    D_AT = ''
    E_AT = ''
    F_AT = ''
    G_AT = ''
    I_AT = ''
    J_AT = ''
    M_AT = ''
    P_AT = ''
    R_AT = ''
    T_AT = ''
    K_AT = ''
    D_FT = ''
    E_FT = ''
    F_FT = ''
    G_FT = ''
    I_FT = ''
    J_FT = ''
    M_FT = ''
    P_FT = ''
    R_FT = ''
    T_FT = ''
    K_FT = ''
    best_guess = ''

    with open('dict/IND_FULL_TO_ABBR_TITLE_CONVERT.dictionary', 'rb') as dictionary_file:
        dictionary = pickle.load(dictionary_file)

    with open('dict/IND_ABBR_TO_FULL_TITLE_CONVERT.dictionary', 'rb') as index_dictionary_file:
        abbr_dictionary = pickle.load(index_dictionary_file)

    with open('dict/IND_FULL_TITLE_TO_INDEX_CONVERT.dictionary', 'rb') as index_dictionary_file:
        index_dictionary = pickle.load(index_dictionary_file)

    while isFound:

        isFound = False
        isLongest = True

        for key in sorted(dictionary.keys(), reverse=True):

            if (TITLE.find(key) == 0 or TITLE.endswith(key)) and isLongest:
                TITLE = TITLE.replace(key, '')
                TITLE = TITLE.strip()
                if index_dictionary[key] == 'D':
                    D_AT = D_AT+dictionary[key]+' '
                    D_FT = D_FT+key+' '
                if index_dictionary[key] == 'E':
                    E_AT = E_AT+dictionary[key]+' '
                    E_FT = E_FT+key+' '
                if index_dictionary[key] == 'F':
                    F_AT = F_AT+dictionary[key]+' '
                    F_FT = F_FT+key+' '
                if index_dictionary[key] == 'G':
                    G_AT = G_AT+dictionary[key]+' '
                    G_FT = G_FT+key+' '
                if index_dictionary[key] == 'I':
                    I_AT = I_AT+dictionary[key]+' '
                    I_FT = I_FT+key+' '
                if index_dictionary[key] == 'J':
                    J_AT = J_AT+dictionary[key]+' '
                    J_FT = J_FT+key+' '
                if index_dictionary[key] == 'M':
                    M_AT = M_AT+dictionary[key]+' '
                    M_FT = M_FT+key+' '
                if index_dictionary[key] == 'P':
                    P_AT = P_AT+dictionary[key]+' '
                    P_FT = P_FT+key+' '
                if index_dictionary[key] == 'R':
                    R_AT = R_AT+dictionary[key]+' '
                    R_FT = R_FT+key+' '
                if index_dictionary[key] == 'T':
                    T_AT = T_AT+dictionary[key]+' '
                    T_FT = T_FT+key+' '
                if index_dictionary[key] == 'K':
                    K_AT = K_AT+dictionary[key]+' '
                    K_FT = K_FT+key+' '
                isFound = True
                isLongest = False
            else:
                pass

        isLongest = True

        for key in sorted(abbr_dictionary.keys(), reverse=True):

            if (TITLE.find(key) == 0 or TITLE.endswith(key)) and isLongest:
                TITLE = TITLE.replace(key, '')
                TITLE = TITLE.strip()
                if index_dictionary[abbr_dictionary[key]] == 'D':
                    D_AT = D_AT+key+' '
                    D_FT = D_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'E':
                    E_AT = E_AT+key+' '
                    E_FT = E_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'F':
                    F_AT = F_AT+key+' '
                    F_FT = F_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'G':
                    G_AT = G_AT+key+' '
                    G_FT = G_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'I':
                    I_AT = I_AT+key+' '
                    I_FT = I_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'J':
                    J_AT = J_AT+key+' '
                    J_FT = J_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'M':
                    M_AT = M_AT+key+' '
                    M_FT = M_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'P':
                    P_AT = P_AT+key+' '
                    P_FT = P_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'R':
                    R_AT = R_AT+key+' '
                    R_FT = R_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'T':
                    T_AT = T_AT+key+' '
                    T_FT = T_FT+abbr_dictionary[key]+' '
                if index_dictionary[abbr_dictionary[key]] == 'K':
                    K_AT = K_AT+key+' '
                    K_FT = K_FT+abbr_dictionary[key]+' '
                isFound = True
                isLongest = False
            else:
                pass

    if TITLE.find('.') > -1 and not TITLE.endswith('.'):
        best_guess = TITLE[0:TITLE.rfind('.')+1]
        TITLE = TITLE[TITLE.rfind('.')+1:]
    AT = I_AT+K_AT+P_AT+M_AT+T_AT+J_AT+D_AT+E_AT+R_AT+F_AT+G_AT+best_guess
    FT = I_FT+K_FT+P_FT+M_FT+T_FT+J_FT+D_FT+E_FT+R_FT+F_FT+G_FT+best_guess
    AT = AT.strip()
    FT = FT.strip()
    TITLE = TITLE.strip()

    p = []
    p.append(AT)
    p.append(FT)
    p.append(TITLE)

    return p


def Preprocess_SID(p):

    # exceptions
    if p.find("test") > -1 or p.find("-") > -1:
        p = SetUnhandle()
    if p.find("ไม่มี") > -1 or p.find("ไม่ลง") > -1 or p.find("ไม่ได้") > -1 or p.find("ไม่ให้") > -1 or p.find("ไม่ยอม") > -1:
        p = SetUnhandle()
    if p.find("ไม่ทรา") > -1 or p.find("ไม่ทรบ") > -1 or p.find("ไม่แจ้ง") > -1 or p.find("ไม่ระบุ") > -1 or p.find("ไม่สะดวก") > -1 or p.find("ไม่ประสงค์") > -1:
        p = SetUnhandle()
    if p.find("ทดสอบ") > -1 or p.find("ยังไม่") > -1 or p.find("ลูกค้าไม่") > -1 or p.find("ลูกค้าใช้") > -1:
        p = SetUnhandle()
    if p.find("บจก.") > -1 or p.find("บจ.") > -1 or p.find("บมจ.") > -1:
        p = SetUnhandle()

    # fix bug-3,4,5
    if p.find("นาย") > -1 and p.find("นาง") > -1:
        p = SetUnhandle()

    # keep thai-english letters number dot and bracket
    p = RemoveSpecialChar(p, flag=True)

    # remove multiple dot
    p = RemoveMultipleDot(p)

    # remove a bracket that contain spaces or other brackets
    p = RemoveEmptyBracket(p)

    # replace tab with space
    p = p.replace('\t', ' ')

    # replace multi space with space
    p = re.sub(' +', ' ', p)

    # remove space at the start and the end of string
    p = p.strip()

    # ณ. อยุธยา, ณ.อยุธยา, ณ อยุธยา
    p = p.replace(' ณ .', ' ณ_')
    p = p.replace(' ณ ', ' ณ_')
    p = p.replace(' ณ. ', ' ณ_')
    p = p.replace(' ณ.', ' ณ_')

    return p


def Postprocess_SID(p):
    if p[4].startswith('ณ_'):
        p[4] = p[3]+' '+p[4]
        p[4] = p[4].strip()
        p[3] = ''

    p[4] = p[4].replace('ณ_', 'ณ ')

    return p


def SplitIndividualName(p):

    # initize string
    AT = ''
    FT = ''
    TT = ''
    FN = ''
    MN = ''
    LN = ''

    # preprocess
    p = Preprocess_SID(p)

    # break title
    t_list = ConcatIndividualTitle(p)
    AT = AT+t_list[0]
    FT = FT+t_list[1]
    AT = AT.rstrip()
    FT = FT.rstrip()
    p = t_list[2]

    # break string to array
    p = p.split(' ')

    # remove duplicate surname
    size = len(p)
    if size > 1:
        if p[size-2] == p[size-1]:
            p = p[:-1]

    # assign First Name(FN), Middle Name(MN), Last Name(LN) by size
    size = len(p)
    if size >= 1:
        if size == 1:
            FN = p[0]
        elif size == 2:
            FN = p[0]
            LN = p[1]
        elif size == 3:
            FN = p[0]
            MN = p[1]
            LN = p[2]
        else:
            FN = p[0]
            MN = p[1]
            for x in range(2, size):
                LN = LN + ' ' + p[x]
    else:
        pass

    p = []
    p.append(AT.strip())
    p.append(FT.strip())
    p.append(FN.strip())
    p.append(MN.strip())
    p.append(LN.strip())

    # postprocess
    p = Postprocess_SID(p)

    return p

# Revise version


def within_margin(keyword, p, margin=3):
    index = p.find(keyword)
    l_index = index
    r_index = abs(len(p)-l_index)-len(keyword)
    min_index = min(l_index, r_index)

    if min_index > -1 and min_index < margin:
        return True
    else:
        return False
    return True


def CheckOrganize(p):

    flag = False

    with open('dict/ORG_FULL_TO_ABBR_TITLE_CONVERT.dictionary', 'rb') as dictionary_file:
        dictionary = pickle.load(dictionary_file)

    for key in sorted(dictionary.keys(), reverse=True):
        #         if p.find(key)>-1 or p.strip().endswith(key):
        if within_margin(key, p):
            flag = True
        else:
            pass

    return flag


def CheckTitle(p):

    flag = False

    with open('dict/IND_FULL_TO_ABBR_TITLE_CONVERT.dictionary', 'rb') as dictionary_file:
        dictionary = pickle.load(dictionary_file)

    for key in sorted(dictionary.keys(), reverse=True):
        #         if p.find(key)>-1 or p.strip().endswith(key):
        if within_margin(key, p):
            flag = True
        else:
            pass

    with open('dict/IND_ABBR_TO_FULL_TITLE_CONVERT.dictionary', 'rb') as dictionary_file:
        dictionary = pickle.load(dictionary_file)

    for key in sorted(dictionary.keys(), reverse=True):
        #         if p.find(key)>-1 or p.strip().endswith(key):
        if within_margin(key, p):
            flag = True
        else:
            pass

    return flag


def Preprocess_SOR(p):

    # remove multiple dot
    p = RemoveMultipleDot(p)

    # remove a bracket that contain spaces or other brackets
    p = RemoveEmptyBracket(p)

    # replace tab with space
    p = p.replace('\t', ' ')

    # replace multi space with space
    p = re.sub(' +', ' ', p)

    # remove space at the start and the end of string
    p = p.strip()

    return p


def Postprocess_SOR(p):

    p[3] = RemoveEmptyBracket(p[3])

    # exception-1
    if p[0].find('บจ.') > -1 and p[0].find('มหาชน') > -1:
        p[0] = 'บมจ.'
    if p[0].find('จำกัด') > -1 and p[0].find('มหาชน') > -1:
        p[0] = 'บมจ.'

    # exception-2
    if p[0] == 'จำกัด':
        p[0] = 'บจ.'
    if p[0].find('จำกัด') > -1:
        p[0] = p[0].replace('จำกัด', '').strip()

    return p


def SetOrganizeName(p):

    OT = ''
    PF = ''
    SF = ''
    has_key = True

    # preprocess
    p = Preprocess_SOR(p)

    # identufy organize title if any
    with open('dict/ORG_FULL_TO_ABBR_TITLE_CONVERT.dictionary', 'rb') as dictionary_file:
        dictionary = pickle.load(dictionary_file)

    while has_key:
        has_key = False
        for key in sorted(dictionary.keys(), reverse=True):
            #             if p.find(key)>-1:
            if within_margin(key, p):
                p = p.replace(key, '')
                p = p.strip()
                OT = OT + ' ' + dictionary[key]
                has_key = True
            else:
                pass
    OT = OT.strip()
    ON = p.strip()

    p = []
    p.append(OT)  # organize title
    p.append('')  # prefix is null
    p.append('')  # suffix is null
    p.append(ON)  # oragnize name

    # postpocess
    p = Postprocess_SOR(p)

    # assign prefix if any
    with open('dict/PREFIX.dictionary', 'rb') as dictionary_file:
        prefix = pickle.load(dictionary_file)
    if p[0] in prefix.keys():
        PF = prefix[p[0]]
    else:
        pass

    # assign suffix if any
    with open('dict/SUFFIX.dictionary', 'rb') as dictionary_file:
        suffix = pickle.load(dictionary_file)
    if p[0] in suffix.keys():
        SF = suffix[p[0]]
    else:
        pass

    p[1] = PF
    p[2] = SF

    return p


# To clean individual and organize name
def Name(p: str):
    '''
    Explain Thai Rule Set (Naming)
    python dict > object serial 
    IND_FULL_TO_ABBR_TITLE_CONVERT.py
        IND_ABBR_TO_FULL_TITLE_CONVERT.dictionary
        IND_FULL_TO_ABBR_TITLE_CONVERT.dictionary
        IND_FULL_TITLE_TO_INDEX_CONVERT.dictionary

    ORG_FULL_TO_ABBR_TITLE_CONVERT.py
        ORG_FULL_TO_ABBR_TITLE_CONVERT.dictionary

    ORG_PREFIX_SUFFIX.py
        PREFIX.dictionary
        SUFFIX.dictionary
    '''
    isTitle_key = ('AT', 'FT', 'FN', 'MN', 'LN')
    isOrganize_key = ('OT', 'PF', 'SF', 'ON')

    isTitle = CheckTitle(p)
    isOrganize = CheckOrganize(p)
    if isTitle and not isOrganize:
        output = SplitIndividualName(p)
        output = {k: v for k, v in zip(isTitle_key, output)}
    if not isTitle and isOrganize:
        output = SetOrganizeName(p)
        output = {k: v for k, v in zip(isOrganize_key, output)}
    if not isTitle and not isOrganize:
        output = SetUnhandle()
        # output = SplitIndividualName(p)
        # output = {k:v for k, v in zip(isTitle_key, output)}
    if isTitle and isOrganize:
        output = SetUnhandle()

    output_dict = {
        'isTitle': isTitle,
        'isOrganize': isOrganize,
        'output': output
    }
    return output_dict


if __name__ == "__main__":
    print(Name('ดีทแฮล์ม แอนด์ โก ลิมิเต็ด'))
    print(Name('บจก. แสงเจริญการไฟฟ้า และ เสียง'))
    print(Name('นาย-นาง สมชัย-พรพรรณ แซ่ลิ้ม-วสุกวิน'))
    print(Name('นายวิชัย. นางนันทนา ตันติวัฒน์พานิช'))
    print(Name('นาย.นาง อัฑฒ์.ชนัญดา พรัดภู่'))
    print(Name('นายชื่อ นามสกุล'))
    # "นายพนพจน์  พวงนาค (สหกรณ์) การเกษตรจำกัด อุบลราชธานี 11120//()((()()))"
