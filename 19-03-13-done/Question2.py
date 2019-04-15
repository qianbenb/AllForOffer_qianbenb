#!/usr/bin/python
# -*- coding: UTF-8 -*-
#股票脱手问题

def Input():
    target_list = input()
    target_list = target_list[1:-1].split(',')
    target_list = [int(x) for x in target_list]
    return target_list

def maxProfit(list):
    length = len(list)
    AllProfit = []
    time = []
    for i in range(length):
        for j in range(i,length):
            Profit = list[j] - list[i]
            AllProfit.append(Profit)
            time.append([i,j])
    MaxProfit = max(AllProfit)
    if MaxProfit < 0:
        return 0
    else:
        return MaxProfit

if __name__ == "__main__":
    list1 = [7,1,5,3,6,4]
    list2 = [7,6,4,3,1]

    print(maxProfit(list1))
    print(maxProfit(list2))

    print(maxProfit(Input()))