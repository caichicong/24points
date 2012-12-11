#!/usr/bin/env python
# -*- coding: utf-8 -*

from itertools import combinations

def bracket_exp(op, a, b):
    return (op, a, b)

def remove_op(ops, op):
    tmp = list(ops)
    tmp.remove(op)
    return tmp

def remove_nums(nums, number_combine):
    tmp = list(nums)
    for i in number_combine:
        tmp.remove(i)
    return tmp

def append(res_nums, exp):
    tmp = list(res_nums)
    tmp.append(exp)
    return tmp


def evalexp(e):
   if not isinstance(e, tuple):
       return int(e)
   else:
       e1 = evalexp(e[1])
       e2 = evalexp(e[2])
       if e1 == None or e2 == None:
           return None
       if e[0] == '+':
           return e1 + e2
       elif e[0] == '-':
           return e1 - e2
       elif e[0] == '*':
           return e1 * e2
       elif e[0] == '/':
           if e2 != 0 and e1 % e2 == 0:
               return e1 / e2
           else:
               return None
       else:
           None

def fmtexp(e):           
   if not isinstance(e, tuple):
       return e
   else:
       e1 = fmtexp(e[1])
       e2 = fmtexp(e[2])
       if e[0] == '+':
           return '(%s + %s)' % (e1, e2) 
       elif e[0] == '-':
           return '(%s - %s)' % (e1, e2) 
       elif e[0] == '*':
           return '(%s * %s)' % (e1, e2) 
       elif e[0] == '/':
           return '(%s / %s)' % (e1, e2) 
       else:
           None

# r = evalexp(('+', '1', ('*', '4', ('-', '6', '8'))))
# r = fmtexp(('+', '1', ('*', '4', ('-', '6', '8'))))

def iter_all_exp(ops, nums, target):
    if len(nums) == 1:
        r = evalexp(nums[0])
        if r and abs(r - target) < 0.001:
            print fmtexp(nums[0]) , '=' + str(target) 
        return
    for number_combine in combinations(nums, 2):
        for op in ops:
            res_ops = remove_op(ops, op)
            res_nums = remove_nums(nums, number_combine)

            exp = bracket_exp(op, number_combine[0], number_combine[1])
            iter_all_exp(res_ops, append(res_nums, exp), target)

            if op == '-' or op == '/':
                exp = bracket_exp(op, number_combine[1], number_combine[0])
                iter_all_exp(res_ops, append(res_nums, exp), target)

iter_all_exp(["+", "-", "/", "*"], ['3', '4', '6', '8'], 24) 
