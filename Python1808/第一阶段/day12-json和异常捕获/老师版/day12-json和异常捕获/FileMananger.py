"""__author__ = 余婷"""
import json


# 1.读取普通文本文件中的内容
def read_text_file(file: str):
    """
    读取指定文件中的内容
    :param file: 文件路径
    :return: 文件中的内容
    """
    try:
        with open(file, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print('警告：文件不存在！！！')
        return ''


# 2.读取json文件中的内容
def read_json_file(file: str):
    """
    读取指定的json文件中的内容
    :param file: 文件地址
    :return: 文件中内容(python数据)
    """
    try:
        with open(file, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('警告：文件不存在！！！')
        return None


# 3.数据写入json文件中
def write_json_file(file, obj):
    """
    数据写入json文件中
    :param file: 文件地址
    :param obj: 写入的python数据
    :return: 是否写入成功
    """
    try:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(obj, f)
            return True
    except:
        return False
