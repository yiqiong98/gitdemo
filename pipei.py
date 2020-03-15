# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:39:07 2019

@author: yiqiong
"""
left=['{','[','(','<']
right=['}',']',')','>']
stack=[]
string=input()
flag=0
for char in string:
    if char in left:
        stack.append(char)
    elif char in right:
        if len(stack)==0:
            flag=1
            break
    if left.index(stack[len(stack)-1])==right.index(char):
        del stack[len(stack)-1]
    else:
        flag=1
        break
if flag==0:
    if len(stack)==0:
        print('yes')
    else:
        print('no')
else:
    print('no')
"""
great!
"""
