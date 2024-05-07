#!/usr/bin/env python3

"""
Jack自定义函数库（42）：
*****************************************************************************
字符串（2）
align_str
    用填充字符sep把字符串str填充到指定占用宽度width，对齐方式align支持左l、中c、右r

format_nan
    将表格的空值转换成''空字符串
*****************************************************************************
数字（2）
is_number
    字符串是否有效数字

sign
    判断数值是正数、负数还是0
*****************************************************************************
输入，输出（6）
input_date
    获取输入的日期并按格式%Y-%m-%d输出，不输默认是今天

pick_from_dict
    输入数字，从字典里获得对应的值

pick_from_dict_v2
    输入数字，从字典里获得对应的键和值

print_all
    打印一个列表里的所有元组的值

print_waiting
    输出等待效果

show_progress
    输出进度
*****************************************************************************
日期时间（9）
format_date
    将date_text从format1转到format2

get_random_date
    获取一个时间范围内的随机日期和时间

get_week_day
    根据指定格式的日期，获取星期几

get_yesterday
    按%Y-%m-%d格式输出指定日期的昨天

is_date_one
    按指定格式进行日期格式校验

is_date
    日期格式校验 - 按通用的5种格式进行检查，只要有一种通过就是合法的日期字符串

now_date
    按%Y-%m-%d格式输出当前日期

now_time
    按%H-%M-%S格式输出当前时间

now_datetime:
    按%Y%m%d%H%M%S格式输出当前日期时间
*****************************************************************************
字典，json（6）
format_cond
    postgresql的条件，在json配置文件里包含数组，转化成可用的元组形式。

get_dict_value(json_dict, key_name)
    Summary:    获取嵌套字典指定key的值
    Arguments:  json_dict:  json嵌套字典
                key_name:   数组，按顺序记录每层key
    Returns:    key_name对应的值

put_dict_value(json_dict, key_name, value)
    Summary:    更新嵌套字典指定key的值
    Arguments:  json_dict:  json嵌套字典
                key_name:   数组，按顺序记录每层key
                value:      更新的值
    Returns:    json_dict

get_rela_value_from_dictlist_by_key
    在一个字典数组里，根据一个属性值找到对应的字典，获取指定的另一批属性的值。

get_value_from_dict
    判断d里是有存在k，存在则返回k的值，不存在返回错误说明s

list_from_dict
    将列表转成字典
*****************************************************************************
加密，流水号（7）
get_chunk_md5(chunk)
    summary:    生成文件分片的MD5
    Arguments:  chunk:  文件分片内容
    Returns:    md5码，如'5deaee1c1332199e5b5bc7c5e4f7f0c2'

get_file_md5(file_path_name, chunkfile_size=-1)
    summary:    生成文件及指定大小分片的MD5
    Arguments:  file_path_name: 文件绝对路径，含文件名
                chunkfile_size: 文件分片大小，MB，默认-1为没有分片
    Returns:    详见代码说明

get_md5
    summary:    生成MD5：非文件
    Arguments:  data:   除文件以外的各种类型的值，如'hello'、17、[1,2,4]、{"a": 1}
    Returns:    md5码，如5deaee1c1332199e5b5bc7c5e4f7f0c2

get_sha1
    获取sha1

get_sha256
    获取sha256

get_sha512
    获取sha512

get_uuid()
    summary: 获取uuid
    Arguments:
    Returns:uuid字符串，去掉'-'
*****************************************************************************
文件（9）
get_file_chunk(file_path_name, chunkfile_size=-1, chunkfile_seq=0)
    summary:    获取文件指定分片的内容
    Arguments:  file_path_name: 文件绝对路径，含文件名
                chunkfile_size: 文件分片大小，MB，默认-1为没有分片
                chunkfile_seq:  第几个文件分片，默认=0
    Returns:    文件内容对象

move_file2bak
    将文件转入同一个路径下的备份目录

read_docx(file)
    读取word DOCX文档（doc不支持）的内容

read_json_file(json_file)
    Summary:    读取json文件，输出字典数据类型
    Arguments:  json_file:  json文件绝对地址
    Returns:    无

write_json_file
    将字典写json文件

read_sql_file
    读取sql文件里的sql语句。一个文件只有一句语句。

urllib_download
    urllib库的方法，下载文件到指定路径；不支持金数据的下载链接。

zipDir
    压缩指定文件夹

upload_baidu(local_path, remote_dir)
    summary:    上传文件到百度网盘
    Arguments:  local_path: 待上传的文件的完整路径（含文件名），如'/Users/jackw/MyPython/test.gif'
                remote_dir: 百度网盘的文件夹完整路径（新文件夹会自动生成），如'/王佳琪工作文档/2022公益之申报名/'
    Returns:    0:  成功
*****************************************************************************
其他（1）
ip_info_ipapi(ip)
    调用ip-api接口获取IP归属地
check_idcard(idcard)
    summary:    校验身份证的有效性
    Arguments:  idcard: 身份证号
    Returns:    1=有效，=0校验位无效，-1=输入不合法
"""


def get_uuid():
    """
    1summary: 获取uuid
    Arguments:
    Returns:uuid字符串，去掉'-'
    """
    import uuid
    return str(uuid.uuid4()).replace('-', '')


def is_date_one(date_text, format_text):
    """
    2summary:按指定格式进行日期格式校验
    Arguments:date_text{string} -- [字符串]
        format_text {string} -- [日期格式，如%Y-%m-%d]
    Returns:
        指定格式的字符串是否是合法日期    {True} -- [是]
                                    {False} -- [不是]
    """
    import time
    try:
        time.strptime(date_text, format_text)
        return True
    except ValueError:
        return False


def is_date(date_text):
    """
    3
    summary:
        日期格式校验 - 按通用的5种格式进行检查，只要有一种通过就是合法的日期字符串
    Arguments:
        date_text {string} -- [字符串]
    Returns:
        字符串是否是合法日期    {True} -- [是]
                            {False} -- [不是]
        哪种日期格式判定为合法日期      {string} -- [
            日期格式目前支持5种:
            '%Y-%m-%d'
            '%Y_%m_%d'
            '%Y%m%d'
            '%Y\\%m\\%d'
            '%Y/%m/%d']
    """
    pattern = ('%Y-%m-%d',
               '%Y_%m_%d',
               '%Y%m%d',
               '%Y\\%m\\%d',
               '%Y/%m/%d',
               '%Y年%m月%d日'
               )
    b = False
    p = ''
    for p in pattern:
        b = is_date_one(date_text, p)
        if b:
            break
        else:
            p = ''
    return b, p


def format_date(date_text, format1, format2):
    """
    4
    summary:
        将date_text从format1转到format2
    Arguments:
        date_text {string} -- [字符串]
        format1 {string} -- [日期格式目前支持5种:
        '%Y-%m-%d'
        '%Y_%m_%d'
        '%Y%m%d'
        '%Y\\%m\\%d'
        '%Y/%m/%d']
        format2 {string} -- [同上]
    Returns:
        转换格式后的日期字符串    {string} -- [如果转换失败，返回'False'字符串]
    """
    from datetime import datetime
    try:
        return datetime.strftime(
            datetime.strptime(
                date_text,
                format1
                ),
            format2
            )
    except ValueError:
        # raise ValueError("Incorrect data")
        return 'False'


def is_number(num_text):
    """
    5
    summary:
        字符串是否有效数字
    Arguments:
        num_text {string} -- [字符串]
    Returns:
        字符串是否是有效数字    {True} -- [是]
                            {False} -- [不是]
    """
    if num_text is None:
        return False
    try:
        float(num_text)
        return True
    except ValueError:
        return False


def sign(num):
    """
    6
    summary:
        判断数值是正数、负数还是0
    Arguments:
        num {数字类型} -- [数值]
    Returns:
        判断数值是正数(1)、负数(-1)还是0(0)
    """
    return (num > 0) - (num < 0)


def now_date():
    """
    7
    summary:
        按%Y-%m-%d格式输出当前日期
    Arguments:
    Returns:
        日期字符串    {string} -- [%Y-%m-%d格式]
    """
    from datetime import datetime
    return datetime.strftime(datetime.today(), '%Y-%m-%d')


def now_time():
    """
    8
    summary:
        按%H:%M:%S格式输出当前时间
    Arguments:
    Returns:
        时间字符串    {string} -- [%H:%M:%S格式]
    """
    from datetime import datetime
    return datetime.strftime(datetime.today(), '%H:%M:%S')


def now_datetime():
    """
    9
    summary:
        按%Y%m%d%H%M%S格式输出当前日期时间
    Arguments:
    Returns:
        日期时间字符串    {string} -- [%Y%m%d%H%M%S格式，纯数字]
    """
    from datetime import datetime
    return datetime.strftime(datetime.today(), '%Y%m%d%H%M%S')


def pick_from_dict(dictValue, title):
    """
    10
    summary:
        输入数字，从字典里获得对应的值
    Arguments:
        dictValue   {dict} -- [字典类型的值]
        title   {string} -- [这批值的名称]
    Returns:
        选中的名称    {string} -- [字典里的value，如果输入值在字典里不存在则退出程序]
    """
    from colorama import Fore, Style

    c = [Fore.CYAN, Fore.MAGENTA]
    i = 0
    print()
    print(Fore.GREEN + "*****" + title + "*****")
    for key, value in dictValue.items():
        print(c[int(i) % 2] + key + " - " + value)
        i = i + 1
    inputValue = input(Fore.YELLOW + "请输入数字：")
    result = dictValue.get(inputValue, 0)
    if result:
        print(Fore.GREEN + result)
        print(Style.RESET_ALL)
        return result
    else:
        print(Fore.RED + title + "输入不正确，程序关闭")
        exit(0)


def pick_from_dict_v2(dictValue, title):
    """
    11
    summary:
        输入数字，从字典里获得对应的键和值
    Arguments:
        dictValue   {dict} -- [字典类型的值]
        title   {string} -- [这批值的名称]
    Returns:
        选中的键值    {string} -- [字典里的key]
        选中的名称    {string} -- [字典里的value，如果输入值在字典里不存在则退出程序]
    """
    from colorama import Fore, Style

    c = [Fore.CYAN, Fore.MAGENTA]
    i = 0
    print(Fore.GREEN + "*****" + title + "*****")
    for key, value in dictValue.items():
        print(c[int(i) % 2] + key + " - " + value)
        i = i + 1
    inputValue = input(Fore.YELLOW + "请输入数字：")
    result = dictValue.get(inputValue, 0)
    if result:
        print(Style.RESET_ALL)
        return inputValue, result
    else:
        print(Fore.RED + title + "输入不正确，程序关闭")
        exit(0)


def format_nan(obj):
    """
    12
    summary:
        将表格的空值转换成''空字符串
    Arguments:
        obj   {string 偶然float} -- [字符类型 或 浮点类型]
    Returns:
        字符    {string} -- [如果输入是浮点且为NaN，则返回''；如果是字符串则原样返回]]
    """
    from numpy import isnan
    if type(obj) == (float):
        if isnan(obj):
            return ''
        else:
            return obj
    else:
        return obj


def move_file2bak(filePath, filename):
    """
    13
    summary:
        将文件转入同一个路径下的备份目录
    Arguments:
        obj   {string or float} -- [字符类型 或 浮点类型]
    Returns:
        字符    {string} -- [如果输入是浮点且为NaN，则返回''；如果是字符串则原样返回]
    """
    from os import mkdir
    from os.path import exists, join
    from shutil import move

    dir = join(filePath, 'bak')
    src = join(filePath, filename)
    dst = join(dir, filename)
    if exists(dir):
        move(src, dst)
    else:
        mkdir(dir)
        move(src, dst)


def print_all(rows_array):
    """
    14
    summary:
        打印一个列表里的所有元组的值；
        20200710：输出增加左对齐，列宽=10
    Arguments:
        rows_array   {list} -- [元素是元组，一个元组有多个值]
    Returns:
        print    {} -- []
    """
    for i in rows_array:
        for j in i:
            print(align_str(str(j), 10, 'l', ' '), end=' ')
            # print(align_str(str(j),10,'l',' ').ljust(10), end=' ')
            # print('{0:{1}<10}\t'.format(str(j),chr(12288)),end = '    ')

        print()


def get_yesterday(date_str):
    """
    15
    summary:
        按%Y-%m-%d格式输出指定日期的昨天
    Arguments:
        date_str    {string} -- [%Y-%m-%d格式的日期]
    Returns:
        日期字符串    {string} -- [%Y-%m-%d格式]
    """
    from datetime import datetime, timedelta
    today = datetime.strptime(date_str, '%Y-%m-%d')
    oneday = timedelta(days=1)
    yesterday = today - oneday
    return datetime.strftime(yesterday, '%Y-%m-%d')


def input_date(tips):
    """
    16
    summary:
        获取输入的日期并按格式%Y-%m-%d输出，不输默认是今天
    Arguments:
        tips   {string} -- [输入提示的补充说明]
    Returns:
        日期字符串    {string} -- [%Y-%m-%d格式]
    """
    if tips:
        tips = tips + '，'
    dateInput = input(tips + "请输入日期（YYYYMMDD）：")
    if is_date(dateInput)[0]:
        dateInput = format_date(dateInput, is_date(dateInput)[1], '%Y-%m-%d')
    else:
        # 不输入，默认当天
        dateInput = now_date()

    return dateInput


def get_week_day(date_str):
    """
    17
    summary:
        根据指定格式的日期，获取星期几
    Arguments:
        date_str   {string} -- [%Y-%m-%d格式]
    Returns:
        日期字符串    {string} -- [%Y-%m-%d格式]
    """
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    from datetime import datetime
    day = datetime.strptime(date_str, '%Y-%m-%d').weekday()
    return week_day_dict[day]


def print_waiting(str):
    """
    18
    summary:
        输出等待效果。尝试，不成熟。
    Arguments:
        str   {string} -- [提示文字]
    Returns:
        打印 str的字符后面带......
    """
    import time
    print(str, end="")
    for i in range(6):
        print(".", end='', flush=True)
        time.sleep(0.2)


def show_progress(current, total, title):
    """
    19
    summary:
        输出进度显示效果。结束为100%。外部调用时要自带循环。
    Arguments:
        current   {int} -- [当前进度值]
        total   {int} -- [总进度值]
        title   {string} -- [进度栏标题]
    Returns:
        显示效果
    """
    import sys
    import time

    progress = round(current * 100.0 / total, 0)
    time.sleep(0.1)
    sys.stdout.write(title + ": %d%% \r" % progress)
    sys.stdout.flush()


def list_from_dict(list):
    """
    20
    summary:
        将列表数组转成key为数字1起始的字典，
        如['a','b','c']=>{'1':'a','2':'b','3':'c'}
    Arguments:
        l   {list} -- [列表]
    Returns:
        字典    {dict} -- [键值为'1'起始]
    """
    return {str(x + 1): list[x] for x in range(len(list))}


def align_str(str, width, align, sep):
    """
    21
    summary:
        用填充字符sep把字符串str填充到指定占用宽度width，对齐方式align支持左l、中c、右r
    Arguments:
        str   {string} -- [待处理的字符串]
        width   {int} -- [处理后的字符串长度]
        align   {string} -- [对齐方式：左l、中c、右r]
        sep   {string} -- [填充字符]
    Returns:
        字符串    {string} -- []
    """
    sigle = 0
    double = 0
    for i in str:
        if len(i.encode('gb2312')) == 1:
            sigle = sigle + 1
        elif len(i.encode('gb2312')) == 2:
            double = double + 1
    t = width * 2 - sigle - double * 2
    if align == 'l':
        return str + t * sep
    elif align == 'r':
        return t * sep + str
    elif align == 'c':
        return t // 2 * sep + str + int(t - t // 2) * sep


def get_value_from_dict(d, k, s):
    """
    22
    summary:
        判断d里是有存在k，存在则返回k的值，不存在返回错误说明s
    Arguments:
        d   {dict} -- [字典]
        k   {string} -- [键]
        s   {string} -- [键的名称]
    Returns:
        键值       {} -- [键对应的值]
    """
    if k in d:
        return d[k]
    else:
        print("错误：" + s + "不存在")
        return 'error'


def get_random_date(start_time, end_time):
    """
    23
    summary:
        在start_time和end_time间（包含）随机获取一天及时间
    Arguments:
        start_time {元组} -- 开始时间，
            比如(2018,8,1,0,0,0,0,0,0) = 2018-08-01 00:00:00
        end_time {元组} -- 结束时间，
            比如(2018,9,30,23,59,59,0,0,0) = 2018-09-30 23:59:59
    Returns:
        日期 时间
    """
    import random
    import time

    # 生成开始时间戳
    start = time.mktime(start_time)
    # 生成结束时间戳
    end = time.mktime(end_time)
    # 在开始和结束时间戳中随机取出一个
    t = random.randint(start, end)
    # 将时间戳生成时间元组
    date_touple = time.localtime(t)
    date = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)

    return date


def get_rela_value_from_dictlist_by_key(data, value, key1, key2):
    """
    24
    summary:
        在一个字典数组里，根据一个属性值找到对应的字典，获取指定的另一批属性的值。
    Arguments:
        data {字典数组} -- 要求字典数组的每个字典的属性都是一样的。
        value {字符串} -- 查询条件的值
        key1 {字符串} -- 查询条件的属性名
        key2 {字符串数组} -- 查询结果的属性名组成的数组
    Returns:
        查询结果的值的数组，与key2顺序一致
    """
    row = {}
    for d in data:
        if d[key1] == value:
            row = d
            break

    rtn = []
    for k in key2:
        if k in row:
            rtn.append(row[k])
        else:
            rtn.append(None)

    return rtn


def read_sql_file(file_name):
    """
    25
    summary:
        读取sql文件里的sql语句。一个文件只有一句语句。
    Arguments:
        file_name {str} -- 文件名，建议绝对地址
    Returns:
        {str} -- 带换行的sql语句
    """
    with open(file_name, 'r') as f:
        sql = f.read()
    return sql


def get_md5(data):
    """
    26
    summary:    生成MD5：非文件
    Arguments:  data:   除文件以外的各种类型的值，如'hello'、17、[1,2,4]、{"a": 1}
    Returns:    md5码，如5deaee1c1332199e5b5bc7c5e4f7f0c2
    """
    import hashlib
    import json
    m5 = hashlib.md5()
    # m5.update(json.dumps(data).encode())  # json.dumps(data)会在字符串外加上""双引号，导致字符串不一致
    m5.update(data.encode())
    return m5.hexdigest()



def get_sha1(data):
    """
    27
    summary:
        生成SHA1
        print(get_sha1("hello"))
        a1f2fbfe2c4ad81749cd0380b735295d06f9d0c4
    Arguments:
    Returns:
    """
    import hashlib
    import json
    s1 = hashlib.sha1()
    s1.update(json.dumps(data).encode())
    return s1.hexdigest()


def get_sha256(data):
    """
    28
    summary:
        生成SHA256
        print(get_sha256("hello"))
        5aa762ae383fbb727af3c7a36d4940a5b8c40a989452d2304fc958ff3f354e7a
    Arguments:
    Returns:
    """
    import hashlib
    import json
    s1 = hashlib.sha256()
    s1.update(json.dumps(data).encode())
    return s1.hexdigest()


# 生成SHA512
def get_sha512(data):
    """
    29
    summary:
        生成SHA512
        print(get_sha512("hello"))
        03ca6996be2fb24e3174b909aee0975a9ebe8be772ff7a525b91d6e647b58c3592ef40efe85b2d7f58d2f9711c2ea115856de2f76e483e57ffe2d9e99ef0100f
    Arguments:
    Returns:
    """
    import hashlib
    import json
    s1 = hashlib.sha512()
    s1.update(json.dumps(data).encode())
    return s1.hexdigest()


def format_cond(json_cond):
    """
    31
    summary:
        postgresql的条件，在json配置文件里包含数组，转化成可用的元组形式。
    Arguments:
        json_cond {数组} -- 如[[313939, 395270], 't']。
    Returns:
        如((313939, 395270), 't')
    """
    r = []
    for p in json_cond:
        if type(p).__name__ == 'list':
            x = tuple(p)
        else:
            x = p
        r.append(x)

    return tuple(r)


def urllib_download(url, folder, name):
    """
    32
    summary:
        urllib库的方法，下载文件到指定路径
    Arguments:
    Returns: 1=成功，0=失败
    """
    import os

    # import traceback

    os.makedirs(folder, exist_ok=True)

    from urllib.request import urlretrieve
    try:
        urlretrieve(url, folder+name)
        print('文件下载成功：' + folder+name)
        return 1
    except Exception as e:
        # traceback.print_exc()
        print('文件下载失败：' + folder+name)
        print(e)
        return 0


def zipDir(dirpath, outFullName):
    """
    33
    压缩指定文件夹
    :param dirpath: 目标文件夹路径，如'./xxxx'
    :param outFullName: 压缩文件名，如'./xxxx.zip'
    :return: 无
    """
    import os
    import zipfile

    zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in filenames:
            zip.write(os.path.join(path, filename),
                      os.path.join(fpath, filename))
    zip.close()
    print('文件夹压缩成功：' + outFullName)


def get_dict_value(json_dict, key_name):
    """
    34
    获取嵌套字典指定key的值
    json_dict: json嵌套字典
    key_name: 数组，按顺序记录每层key
    return: 键值
    """
    for i in key_name:
        if i in json_dict:
            r = json_dict[i]
            json_dict = json_dict[i]
        else:
            r = None
    return r


def put_dict_value(json_dict, key_name, value):
    """
    35
    更新嵌套字典指定key的值
    json_dict: json嵌套字典
    key_name: 数组，按顺序记录每层key
    value: 更新的值
    return: json_dict
    """
    s = "json_dict"
    for i in key_name:
        s = s + f"['{i}']"

    if type(value).__name__ == 'str':
        value = "'" + value + "'"

    exec(f"{s}={value}")

    return json_dict


def read_json_file(json_file):
    """
    36
    读取json文件，输出字典数据类型
    """
    import json
    with open(json_file, 'r') as f:
        j = json.load(f)
    return j


def write_json_file(json_file, new_dict):
    """
    37
    将字典写json文件
    """
    import json
    with open(json_file, 'w') as f:
        json.dump(new_dict, f, ensure_ascii=False)
        # 不写ensure_ascii=False，写进json文件的中文是转义码，如\u4e66\u6cd5


def get_file_md5(file_path_name, chunkfile_size=-1):
    """
    38
    summary:    生成文件及指定大小分片的MD5
    Arguments:  file_path_name: 文件绝对路径，含文件名
                chunkfile_size: 文件分片大小，MB，默认-1为没有分片
    Returns:    {
                    "file": "/Users/jackw/MyPython/test.gif", 完整文件名
                    "total_size": 13178538, 文件大小，字节
                    "chunk_size": 4194304,  分片大小，字节
                    "total_chunk": 4,   分片数
                    "chunk_list": [ 分片列表
                        {
                            "seq": 0,   序号
                            "start": 0, 分片起始位置
                            "end": 4194304, 分片结束为止
                            "md5": "6539853b159be706a81b2e77bdcd8412"   分片md5
                        },
                        {
                            "seq": 1,
                            "start": 4194304,
                            "end": 8388608,
                            "md5": "2eb8672729cde385cb36a43221452303"
                        },
                        {
                            "seq": 2,
                            "start": 8388608,
                            "end": 12582912,
                            "md5": "1113258b7e0b22456dcc086a3acaf033"
                        },
                        {
                            "seq": 3,
                            "start": 12582912,
                            "end": 13178538,
                            "md5": "84929e4a5e81a302a28d10a00e11218a"
                        }
                    ]
                }
    """
    import hashlib
    import math
    import os

    total_size = os.path.getsize(file_path_name)
    if chunkfile_size <= 0:
        chunk_size = total_size
    else:
        chunk_size = 1024 * 1024 * chunkfile_size
    total_chunk = math.ceil(total_size / chunk_size)

    chunk_list = []
    file_md5 = ''

    with open(file_path_name, 'rb') as f:
        # 全文件md5
        m5 = hashlib.md5()
        for line in f:
            m5.update(line)
        file_md5 = m5.hexdigest()

        # 分片
        current_chunk = 1
        while current_chunk <= total_chunk:
            m5 = hashlib.md5()
            chunk_item = {}

            start = (current_chunk - 1) * chunk_size
            end = min(total_size, start + chunk_size)

            f.seek(start)
            file_chunk_data = f.read(end - start)
            m5.update(file_chunk_data)
            chunk_md5 = m5.hexdigest()

            chunk_item['seq'] = current_chunk - 1
            chunk_item['start'] = start
            chunk_item['end'] = end
            chunk_item['md5'] = chunk_md5
            chunk_list.append(chunk_item)

            # md5_list = [x['md5'] for x in chunk_list if x.get('md5')]

            current_chunk = current_chunk + 1

    f.close()
    rtn = {
        'file': file_path_name,
        'file_md5': file_md5,
        'total_size': total_size,
        'chunk_size': chunk_size,
        'total_chunk': total_chunk,
        'chunk_list': chunk_list
    }
    return rtn


def get_file_chunk(file_path_name, chunkfile_size=-1, chunkfile_seq=0):
    """
    39
    summary:    获取文件指定分片的内容
    Arguments:  file_path_name: 文件绝对路径，含文件名
                chunkfile_size: 文件分片大小，MB，默认-1为没有分片
                chunkfile_seq:  第几个文件分片，默认=0
    Returns:    文件内容对象
    """
    import os

    total_size = os.path.getsize(file_path_name)
    if chunkfile_size <= 0:
        chunk_size = total_size
    else:
        chunk_size = 1024 * 1024 * chunkfile_size

    with open(file_path_name, 'rb') as f:
        start = chunkfile_seq * chunk_size
        end = min(total_size, start + chunk_size)
        f.seek(start)
        file_chunk_data = f.read(end - start)

    f.close()
    return file_chunk_data


def get_chunk_md5(chunk):
    """
    40
    summary:    生成文件分片的MD5
    Arguments:  chunk:  文件分片内容
    Returns:    md5码，如'5deaee1c1332199e5b5bc7c5e4f7f0c2'
    """
    import hashlib
    m5 = hashlib.md5()
    m5.update(chunk)
    md5code = m5.hexdigest()
    return md5code


def upload_baidu(local_path, remote_dir):
    """
    41
    summary:    上传文件到百度网盘
    Arguments:  local_path: 待上传的文件的完整路径（含文件名），如'/Users/jackw/MyPython/test.gif'
                remote_dir: 百度网盘的文件夹完整路径（新文件夹会自动生成），如'/王佳琪工作文档/2022公益之申报名/'
    Returns:    0:  成功
    """
    import os

    import demjson

    import jacklib
    import jacklib_baidupan as bdp

    print('上传开始于：' + jacklib.now_date() + ' ' + jacklib.now_time())

    file_name = local_path.split('/')[-1:][0]
    remote_path = os.path.join(remote_dir, file_name)
    file_ret = jacklib.get_file_md5(local_path, 4)
    block_list = demjson.encode(
        [x['md5'] for x in file_ret['chunk_list'] if x.get('md5')])
    print('上传切片完成：' + jacklib.now_date() + ' ' + jacklib.now_time())

    access_token = bdp.refresh_token()
    print('百度盘access_token刷新完成：' + jacklib.now_date() + ' ' + jacklib.now_time())

    pre_create_file_ret = bdp.pre_create_file(
        access_token,
        remote_path,
        local_path,
        block_list
    )
    print('预上传完成：' + jacklib.now_date() + ' ' + jacklib.now_time())

    uploadid = pre_create_file_ret['uploadid']
    block_seq_list = pre_create_file_ret['block_list']

    for q in block_seq_list:
        bdp.part_upload(
            access_token,
            remote_path,
            uploadid,
            q,
            local_path)

        print('第' + str(q+1) + '个分片上传完成：' + jacklib.now_date() + ' ' + jacklib.now_time())

    bdp.create_remote_file(
        access_token,
        remote_path,
        uploadid,
        block_list,
        local_path
    )

    print('上传结束于：' + jacklib.now_date() + ' ' + jacklib.now_time())


def ip_info_ipapi(ip):
    """
    42
    summary:    调用ip-api接口获取IP归属地
    Arguments:  ip：ip地址
    Returns:    {'status': status,
                'country': country,
                'province': province,
                'city': city,
                'isp': isp}
    """
    import requests
    url = 'http://ip-api.com/json/' + ip
    ret = requests.get(url)
    ret = ret.json()

    status = ret['status']
    if status == 'success':
        return {'status': status,
                'country': ret['country'],
                'province': ret['regionName'],
                'city': ret['city'],
                'isp': ret['isp']}
    else:
        return {'status': status}


def read_docx(file):
    """
    43
    summary:    读取word DOCX文档（doc不支持）的内容
    Arguments:  file: docx文件绝对地址
    Returns:    字符串，段落换行
    """
    from docx import Document

    doc = Document(file)
    txt = ''
    for paragraph in doc.paragraphs:
        txt = txt + paragraph.text + '\n'
    return txt


def check_idcard(idcard):
    """
    44
    summary:    校验身份证的有效性
    Arguments:  idcard: 身份证号
    Returns:    1=有效，=0校验位无效，-1=输入不合法

    身份证校验规则：
    1. 将身份证号码的前17位数字分别乘以数组中对应位置的数字，得到17个乘积结果。
    2. 将这17个乘积结果相加，得到一个总和。
    3. 将这个总和除以11，得到一个余数。
    4. 根据余数在一个特定的映射表中查找对应的校验码，将其作为身份证号码的最后一位校验码。
    """
    idcard = idcard.strip().upper()

    if not idcard[:17].isdigit():
        return -1

    if len(idcard) == 18:
        list1 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        list2 = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        s = 0 # 加权求和值
        i = 0

        for n in idcard[:17]:
            s += int(n) * list1[i]
            i += 1

        s = s % 11
        v = list2[s] # 最后的校验位

        if v == idcard[17]:
            return 1
        else:
            return 0
    else:
        return -1


# def log(content, filename):
#     """
#     45
#     summary:    记录日志
#     Arguments:  content: 日志内容
#                 filename: 日志文件名
#     Returns:    生成并写入文件
#     """
#     import logging
#
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.INFO)  # 根据需要设置合适的日志级别
#
#     # 创建文件处理器
#     file_handler = logging.FileHandler(filename)  # 指定日志文件路径和名称
#
#     # 设置日志格式
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)
#
#     # 将文件处理器附加到记录器
#     logger.addHandler(file_handler)
#
#     logger.debug("This is a debug message.")
#     logger.info("This is an info message.")
#     logger.warning("This is a warning message.")
#     logger.error("This is an error message.")
#     logger.critical("This is a critical message.")



