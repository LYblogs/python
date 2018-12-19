import json
# 1.读取普通文本文件的内容
def read_text_file(file:str):
    """
    读取指定文件中的内容
    :param file: 文件地址
    :return: 文件中的内容
    """
    try:
        with open(file,encoding="utf-8")as  f:
            return f.read()
    except FileNotFoundError:
        return ""
# 2.读取json文件中的内容
def read_json_file(file:str):
    """
    读取指定json文件中的内容
    :param file: 文件地址
    :return: 文件中的内容（python数据）
    """
    try:
        with open(file,encoding="utf-8")as f:
            return json.load(f)
    except FileNotFoundError:
        return None

#3.将数据写入json文件中

def write_json_file(file,obj):
    """
    将数据写入json文件中
    :param file: 文件地址
    :param obj: 写入的数据
    :return: 是否写入成功
    """
    try:
        with open(file,"w",encoding="utf-8")as f:
            json.dump(obj,f)
            return True
    except:
        print("写入失败！")
        return False