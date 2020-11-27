import os
import sys
import numpy as np
import pandas as pd
from datetime import datetime
from argparse import ArgumentParser

commas = '.' * 100
_verbose = []


def isValid(folder_path, ):
    if os.path.isdir(folder_path):
        print("directory exists")
        return 1
    else:
        print("directory not exists")
        return 0
    pass


def build_test_files(test_dir=r"path", file_num=100, ):
    """
    This function is going to build a bunch of files within random texts..., and add targets/key words to be probed.
    """
    flg = 0
    txt = '125ake;ghowijetg;awlkej ;lwakej;wlaej;wlaejr;kaweht;awentggsgE'

    if not isValid(test_dir):
        return

    for _ in range(file_num):
        tmp = open(test_dir + '{}.txt'.format(_), 'w')  # open file as write

        # how many lines to be written
        line_num = np.random.randint(1000)
        for __ in range(line_num):
            
            # how many character to be written 
            char_num = np.random.randint(len(txt))
            tmp.write('{}\n'.format(txt[:char_num]))
            
            # add targets/key words
            # add "hello world" if char_num > 80 , add "goodbye world" elif char_num > 300 
            if __ > 80 and flg == 0:
                flg = 1
                tmp.write('hello world\n')
            elif __ > 300 and flg == 1:
                flg = 2
                tmp.write('goodbye world\n')
        flg = 0
    pass


def findLog(*contains, folder_path=r"path", save_path=r"path"):

    # check folder is existed?
    if not isValid(folder_path):
        return

    _res = {}
    _buf = {}
    global _verbose

    # get the list of all files and directories in the specified directory
    files = os.listdir(folder_path)

    # use dict to store lines prevent from duplicates
    for file in files:
        try:
            tmp_file = folder_path + str('\\') + file
            with open(tmp_file, "r", encoding='utf-8') as _tmp_file:
                data = _tmp_file.readlines()
                
                # build a dict{key: set()} 
                # dict
                # >>> {'abc': {'file1', 'file2',..}, ...}
                for line in data:
                    if not _buf.get(line):
                        _buf[line] = {file}
                    else:
                        _buf[line].add(file)

        # record error
        except Exception as e:
            _verbose.append(e.__str__() + "\n")
            pass

    # iterate keys, to find intersection of line of _buf and contains
    folder_name = os.getcwd().split(os.sep)[-1]

    for line in _buf.keys():
        for tar in contains:
            if tar.lower() in line.lower():
                log = _buf[line].pop()
                _res[folder_name + ',' + log] = tar
        pass

    # if intersection is True, write log file
    if len((_res.values())):

        # write data to my path
        log = pd.DataFrame.from_dict(_res, orient='index')
        log.to_csv(path_or_buf=save_path + r"{folder}.csv".format(folder=folder_name))
        _verbose.append("Save " + commas + "\n")

        w = open(save_path + '{folder}.log'.format(folder=folder_name), 'w')
        for _ in _verbose:
            w.write(_)
        w.close()

    pass


# customized
def processTable(file_dir=r"path",):
    file = os.listdir(file_dir)
    file_name = set()
    for f in file:
        file_name.add(f[:-4])

    tmp = []

    for i in file_name:
        f = file_dir + "\\" + i + '.csv'
        tmp.append(pd.read_csv(f))
    df = pd.concat(tmp)
    df.sort_values(by=['0'])

    df.columns = ['msg', 'hostname']
    df['folder'] = df.apply(lambda x: x.msg.split(',')[0], axis=1)
    df['log_name'] = df.apply(lambda x: x.msg.split(',')[1], axis=1)
    df['datetime'] = df.apply(lambda x: x.msg.split(',')[1][:-4], axis=1)

    df = df.drop('msg', axis=1)
    df.sort_values(by=['hostname', 'datetime'])

    df.to_csv(file_dir + r"\\" + 'table.csv', index=False)


# test
if __name__ == '__main__':

    folders = os.listdir(file_dir)

    # for folder in folders:
    #     _verbose.append(("Folder Name: {} ".format(folder) + commas)[:100])
    #     findLog('file1', 'file2', 'file3', 'file4', 'file5', 'file6', 'file7', 'file8',
    #             file_dir=file_dir, folder=folder, )
    #
    # processTable(file_dir=savePath)

    """
    f_dir = r"\\folder1\Logs\"
    folder = 'Begin Install-Validate Install'
    findLog('file',
            file_dir=f_dir, folder=folder)
    >>> ???
    """

    pass

