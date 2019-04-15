#!/usr/bin/python
# -*- coding: UTF-8 -*-
#字符串问题

def isMatch( s, p):
    if p == "":
        return s == ""
    if len(p) > 1 and p[1] == "*":
        return isMatch(s, p[2:]) or (s and (s[0] == p[0] or p[0] == '.') and isMatch(s[1:], p))
    else:
        return s and (s[0] == p[0] or p[0] == '.') and isMatch(s[1:], p[1:])

if __name__ == '__main__':
    print(isMatch("aa", "a"))
    print(isMatch("aab", "c*a*b"))
    print(isMatch("mississippi", "mis*is*p*."))
