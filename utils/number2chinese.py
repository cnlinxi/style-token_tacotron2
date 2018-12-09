# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 9:42
# @Author  : MengnanChen
# @FileName: number2chinese.py
# @Software: PyCharm

from __future__ import unicode_literals

import re


def number2chinese(number):
    """整型数字转汉字
    """
    # 只能到千亿
    if not isinstance(number, (int,)) or number < 0 or number >= pow(10, 12):
        return None
    if number == 0:
        return '零'

    digit_to_hanzi = {
        '0': '零',
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
        '8': '八',
        '9': '九',
    }
    # 每四位
    sections = {
        4: '万',
        8: '亿',
    }
    # 1~999 的读法；比如 350 -> 3百, 5十
    per_section = {
        1: '十',
        2: '百',
        3: '千',
    }
    number_string = str(number)

    def convert_four_number(num):
        """此时传入的num已经是倒叙
        """
        res = ''
        for i, val in enumerate(num):
            tmp = digit_to_hanzi.get(val)
            if val != '0':
                tmp += per_section.get(i % 4, '')
            res = tmp + res
        return res

    result = []
    four_number_round = ''
    total_count = len(number_string)
    for i, val in enumerate(reversed(number_string)):
        if i in sections:
            result.insert(0, sections[i])
        # 每4位
        four_number_round += val
        if len(four_number_round) < 4 and i+1 < total_count:
            continue

        insert_val = convert_four_number(four_number_round)
        # 末4位直接放进去
        if i < 4:
            insert_val = insert_val.rstrip('零')
        # 全零的话，把上一次的'万', '亿'替换为'零'
        elif all([i == '零' for i in insert_val]):
            result[0] = '零'
        # 非全零，且以零结尾
        # 则：结尾的多个零合并为一个零，且与'万'或'亿'位置置换
        elif insert_val.endswith('零'):
            insert_val = insert_val.rstrip('零')
            pos_zero = result.pop(0)
            insert_val = insert_val + pos_zero + '零'

        result.insert(0, insert_val)
        four_number_round = ''
    result = ''.join(result)

    # 10: 一十 -> 十
    # 10,0000: 一十万 -> 十万
    if result.startswith('一十'):
        result = result.lstrip('一')

    # 首尾多余的'零'
    result = result.strip('零')
    # 1001: 一千零零一 -> 一千零一
    result = re.sub(r'零+', '零', result)

    return result


if __name__ == '__main__':
    print(number2chinese(106))
