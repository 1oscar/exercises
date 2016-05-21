#!/usr/bin/env python
#coding=utf8

def func(inputNum):
    eleList = [100,50,20,10,5,1]
    inputNum1 = inputNum
    a=0
    he=0
    num = 0
    result = dict()
    for i in range(6):
        if(eleList[i]==0):
            break
        if(inputNum/eleList[i]>0):
            
            
            he = inputNum/eleList[i]*eleList[i]
            result[eleList[i]] = inputNum/eleList[i]
            
            inputNum = inputNum - he
            num = num+1
        else:
            
            if(inputNum%eleList[i] == 0):
                result[eleList[i]] = inputNum%eleList[i]
                num = num+1
               


    return num,result
def main():
    num,result = func(20)
    print sum(result.values())

main()