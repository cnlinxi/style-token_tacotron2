# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 15:35
# @Author  : MengnanChen
# @FileName: check_min_samples.py
# @Software: PyCharm

import random


def main(input_path,output_path,sample_rate=0.5):
    with open(input_path,'rb') as fin,open(output_path,'wb') as fout:
        all_samples=fin.readlines()
        sample_samples=random.sample(all_samples,int(sample_rate*len(all_samples)))
        fout.writelines(sample_samples)


if __name__ == '__main__':
    sample_rate=0.5
    input_path='../training_data/train.txt'
    output_path='../training_data/train{}.txt'.format(sample_rate)
    main(input_path,output_path,sample_rate)