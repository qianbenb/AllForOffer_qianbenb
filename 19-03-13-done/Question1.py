#!/usr/bin/python
# -*- coding: UTF-8 -*-
#水池找面积最大问题

def Input():
    target_list = input()
    target_list = target_list[1:-1].split(',')
    target_list = [int(x) for x in target_list]
    return target_list

def maxArea(list):
    length = len(list)
    AllArea = []
    for i in range(length):
        for j in range(length):
            Area = abs( i - j ) * min(list[i], list[j])
            AllArea.append(Area)
    MaxArea = max(AllArea)
    return MaxArea

if __name__ == '__main__':
    list = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(maxArea(list))
    print(maxArea(Input()))