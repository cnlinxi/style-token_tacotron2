# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 10:29
# @Author  : MengnanChen
# @FileName: datasets_statics.py
# @Software: PyCharm

import re
from copy import deepcopy

from pyhanlp import *


def statics_dataset_biaobei(input_path, output_path):
    # {'word':{'nature':[],'mark':[]},...}
    word_dict = dict()
    all_nature_set=set()
    _chi_re = re.compile(r'([\u4e00-\u9fa5]+?)#([1-4]?)(.*)')
    _replacement_expression = [(re.compile('{}'.format(x[0]), re.IGNORECASE), x[1]) for x in [
        ('#1', ''),
        ('#2', ''),
        ('#3', ''),
        ('#4', ''),
    ]]

    with open(input_path, 'rb') as fin:
        for line in fin:
            line = line.decode('utf-8').strip('\r\n ')

            line_cleaned = deepcopy(line)
            for regex, replacement in _replacement_expression:
                line_cleaned = re.sub(regex, replacement, line_cleaned)
            for term in HanLP.segment(line_cleaned):
                if term.word not in word_dict.keys():
                    word_dict[term.word] = {'nature': [], 'mark': []}
                word_dict[term.word]['nature'].append(term.nature)
                all_nature_set.union(term.nature)

            while len(line):
                m = _chi_re.match(line)
                if not m:
                    break
                if m.group(1) not in word_dict.keys():  # word
                    word_dict[m.group(1)] = {'nature': [], 'mark': []}
                word_dict[m.group(1)]['mark'].append(m.group(2))  # mark
                line = m.group(3)  # other content in line

    mark_statics_dict={}  # {'mark':{'n':1,'v':2,...},...}
    for k,v in word_dict:  # k: word, v: {'nature':[],'mark':[]}
        if len(v['nature'])!=len(v['mark']):
            print('<{}> wordcut not match'.format(k))
            continue
        if len(set(v['nature']))>1:
            print('<{}> have {} natures: {}'.format(k,len(set(v['nature'])),','.join(list(set(v['nature'])))))
        if len(set(v['mark']))>1:
            print('<{}> have {} marks: {}'.format(k,len(set(v['mark'])),','.join(list(set(v['mark'])))))
        for nature,mark in zip(v['nature'],v['mark']):
            if mark not in mark_statics_dict.keys():
                mark_statics_dict[mark]=dict()
            if nature not in mark_statics_dict[mark].keys():
                mark_statics_dict['mark']
