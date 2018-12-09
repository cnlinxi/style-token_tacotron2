# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 17:30
# @Author  : MengnanChen
# @FileName: biaobei_cleaner.py
# @Software: PyCharm

import re
from pypinyin import lazy_pinyin, Style

_replacement_expression = [(re.compile('{}'.format(x[0]), re.IGNORECASE), x[1]) for x in [
    ('# 1', 'A'),
    ('# 2', 'B'),
    ('# 3', 'C'),
    ('# 4', 'D'),
    ('-','至')
]]


def biaobei_cleaner(input_path, output_path):
    output_lines = []
    index=1
    with open(input_path, 'rb') as fin, open(output_path, 'wb') as fout:
        for line in fin:
            line = line.decode('utf-8').strip('\r\n ')
            line = ' '.join(lazy_pinyin(line, style=Style.TONE2))
            for regex, replacement in _replacement_expression:
                line = re.sub(regex, replacement, line)
            line = '{:05d}|{}\n'.format(index,line)
            output_lines.append(line.encode('utf-8'))
            index+=1
        fout.writelines(output_lines)


if __name__ == '__main__':
    input_path='data/out_hanzi.txt'
    output_path='data/biaobei.corpus'
    biaobei_cleaner(input_path,output_path)
