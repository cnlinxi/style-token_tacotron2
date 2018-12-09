# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 17:53
# @Author  : MengnanChen
# @FileName: rm_files.py
# @Software: PyCharm

import os

for i in range(126000,174000,2000):
    print('remove {}'.format(i))
    os.remove('waveglow_{}'.format(i))