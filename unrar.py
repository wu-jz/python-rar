import difflib
import os
import shutil
from unrar import rarfile


# 获取列表的第二个元素
def take_second(elem):
    return elem[1]


def unrar_file(file_path, out_path):
    rf = rarfile.RarFile(file_path)
    rf.extractall(out_path)


# 获取指定路径下所有的文件，并过筛选相应文件
def all_path(dir_path, dir_name):
    # 设置过滤后的文件类型 当然可以设置多个类型
    file_filter = [".doc", ".docx"]
    result = []
    # maindir(当前主目录)   subdir(当前主目录下的所有目录)  file_name_list(当前主目录下的所有文件)
    for maindir, subdir, file_name_list in os.walk(dir_path):
        for filename in file_name_list:
            # 合并成一个完整路径
            com_path = os.path.join(maindir, filename)
            # 获取文件后缀 [0]获取的是除了文件名以外的内容
            ext = os.path.splitext(com_path)[1]
            # 过滤文件
            if ext in file_filter:
                # 比较该文件与压缩文件名相似度
                num = difflib.SequenceMatcher(None, filename, dir_name).quick_ratio()
                result.append([com_path, num])
    # 获取相似度最高的数据
    result.sort(key=take_second, reverse=True)
    if len(result) != 0:
        result = result[0]
    return result


def do_unrar(path):
    # 获取文件路径
    dir_path = os.path.dirname(path)
    # 获取文件名称
    dir_name = os.path.basename(path)
    temp_out_path = dir_path + "\\" + dir_name
    try:
        # 进行解压操作
        unrar_file(path, temp_out_path)
        # 进行解压文件过滤操作
        file_list = all_path(temp_out_path, dir_name)
        # 将最终文件移至当前文件夹
        if len(file_list) != 0:
            return shutil.copy(file_list[0], dir_path)
        return None
    except Exception as e:
        print(e)
    finally:
        # 删除临时文件
        shutil.rmtree(temp_out_path)


if __name__ == '__main__':
    res = do_unrar("G:\\rar\\file\\test.rar")
