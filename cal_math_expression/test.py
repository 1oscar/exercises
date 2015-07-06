#!/usr/bin/env python
#coding=utf8

import operator
import traceback

#逆波兰表达式求值: 
#https://zh.wikipedia.org/wiki/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E7%A4%BA%E6%B3%95

def cal_list(l):

    res_list = []
    
    for i in range(len(l)):
        if l[i] not in ['+', '-', '*', '/']:
            res_list.append(l[i])
        elif l[i] in ['+', '-', '*', '/']:
            val1 = res_list.pop()
            try:
                val2 = res_list.pop()
            except:
                val2 = l[i+1]
                #print l[i+1]
                print '不是逆波兰表示法'
            
            #print val2
            if l[i] is '+':
                result = operator.add(int(val1), int(val2))
                print result
            elif l[i] is '*':
                result = operator.mul(int(val1), int(val2))
                print result
            elif l[i] is '-':
                #print l[i]+val2
                result = operator.add(int(l[i]+val1), int(val2))
            elif l[i] is '/':
                if val1 is '0':
                    print '被除数不能为0, aaaa'
                result = operator.div(int(val2), int(val1))
                #print result

            res_list.append(str(result))
        else:
            print 'input operator in list have errors'
            traceback.print_exc()
    
    if len(res_list) == 1:
        print '\nthe list expersion result:', res_list.pop()


if __name__ == '__main__':
    
    '''
    s = raw_input('Enter your calculate list, 请以逗号分割，不要空格:\n')
    l = s.split(',')
    '''
    #l = ['3', '4', '-', '5', '*']
    l = ['3', '13', '5', '/', '+']
    l = ['3', '4', '+', '*', '5']   #不是逆波兰表示法 
    cal_list(l)
