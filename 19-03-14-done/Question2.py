#!/usr/bin/python
# -*- coding: UTF-8 -*-
#找最长的回文子串

def LongestSubStr(s):
    k = len(s)
    matrix = [[0 for i in range(k)] for i in range(k)]
    logestSubStr = ""
    logestLen = 0

    for j in range(0, k):
        for i in range(0, j + 1):
            if j - i <= 1:
                if s[i] == s[j]:
                    matrix[i][j] = 1
                    if logestLen < j - i + 1:
                        logestSubStr = s[i:j + 1]
                        logestLen = j - i + 1
            else:
                if s[i] == s[j] and matrix[i + 1][j - 1]:
                    matrix[i][j] = 1
                    if logestLen < j - i + 1:
                        logestSubStr = s[i:j + 1]
                        logestLen = j - i + 1
    return logestSubStr

# if __name__ == '__main__':
#     print(LongestSubStr('google'))
#     print(LongestSubStr('cbbd'))

A = [1,2,3,4,5,6,7]
print A[0:2]