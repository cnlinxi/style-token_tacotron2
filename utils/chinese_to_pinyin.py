# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 16:37
# @Author  : MengnanChen
# @FileName: chinese_to_pinyin.py
# @Software: PyCharm

from pypinyin import lazy_pinyin, Style


def transform_chinese_to_pinyin(data_path, output_path,type='corpus'):
    with open(data_path, 'rb') as fin, open(output_path, 'wb') as fout:
        if type=='corpus':
            for line in fin:
                line = line.decode('utf-8').strip('\r\n ')
                if not line:
                    continue
                transformed_line = ' '.join(lazy_pinyin(line, style=Style.TONE2))
                fout.write(f'{transformed_line}\n'.encode('utf-8'))
        elif type=='training_data':
            for line in fin:
                line=line.decode('utf-8').strip('\r\n ')
                if not line:
                    continue
                index,chinese_text=line.split('|')
                pinyin_text=' '.join(lazy_pinyin(chinese_text,style=Style.TONE2))
                fout.write(f'{index}|{pinyin_text}\n'.encode('utf-8'))


if __name__ == '__main__':
    # data_dir = 'data/inputs.txt'
    # output_dir = 'data/pinyin.corpus'
    data_path='female_golden_v2/female_golden_v2.txt'
    output_path='female_golden_v2/female_golden.corpus'
    type='training_data'
    transform_chinese_to_pinyin(data_path, output_path,type=type)