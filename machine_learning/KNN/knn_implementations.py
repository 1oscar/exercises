#!/usr/bin/env python
#coding=utf8

'''
    @date: 2015-07-14
    @author: 段家公子
    @desc: implementations k nearest algorithms

'''

import csv
import operator
import random
import math

'''
load_file load file, 小于0.67的作为训练集合，大于0.67的作为测试集。训练集合于测试集合约等于2:1
'''
def load_file(file_name, split_criterion):

    print dir(csv)
    
    train_sets = []
    test_sets = []
    with open(file_name, 'r') as csv_file:
        content = csv.reader(csv_file)
        data_sets = list(content)
        for i in range(len(data_sets)):
            for j in range(4):
                data_sets[i][j] = float(data_sets[i][j])
            if random.random() < split_criterion:
                train_sets.append(data_sets[i])
            else:
                test_sets.append(data_sets[i])
    print len(train_sets)
    print len(test_sets)
    return train_sets, test_sets

'''
for i in range(len(instance1)): 维度计算，各个维度都要计算
'''
def cal_distance(instance1, instance2):
    result = 0
    #test_instance[-1] : --> Iris** can't computer
    for i in range(len(instance1)-1):
        result += math.pow(instance1[i] - instance2[i], 2)
    result = math.sqrt(result)
    return result

'''
>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
>>> student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
'''
'''
>>> itemgetter(1)('ABCDEFG')
'B'
>>> itemgetter(1,3,5)('ABCDEFG')
('B', 'D', 'F')
>>> itemgetter(slice(2,None))('ABCDEFG')
'CDEFG'
'''
def get_k_neighbors(train_sets, test_instance, k):
    #print '\n\n' 
    #print  train_sets
    #print test_instance
    #print len(train_sets)
    distance = []
    for i in range(len(train_sets)):
        result = cal_distance(train_sets[i], test_instance)
        result = round(result, 3)
        distance.append((train_sets[i], result))
    #print distance[:3]
    #reverse=True: desc降序没有则是默认asc升序; 按照第二个参数排序
    '''
    distance.sort(key=lambda x:x[1])
    或者
    distance.sort(key=operator.itemgetter(1))
    '''
    distance.sort(key=lambda x:x[1], reverse=False)
    #print distance[:3]
    k_nearest_sets = []
    for j in range(int(k)):
        k_nearest_sets.append(distance[j][0])
    #print k_nearest_sets
    return k_nearest_sets


def label_predict(k_nearest_sets):
    count_dict = {}
    
    for i in range(len(k_nearest_sets)):
        reponse = k_nearest_sets[i][-1]
        if reponse in count_dict:
            count_dict[reponse] += 1
        else:
            count_dict[reponse] = 1
    #print 'before sort:', count_dict
    sort_vote = sorted(count_dict.iteritems(), key=lambda x:x[1], reverse = True)
    
    #print 'after sort: ', sort_vote
    return sort_vote[0][0]


def get_accuracy(test_sets, predict_sets):
    count = 0
    for i in range(len(test_sets)):
        if test_sets[i][-1] == predict_sets[i]:
            count += 1
        else:
            pass
    return (count/float(len(test_sets)))*100.0
    


if __name__ == '__main__':
    file_name = './iris.data'
    split_criterion = 0.67
    k = 3
    train_sets, test_sets = load_file(file_name, split_criterion)
    print len(test_sets)
    predict_sets = []
    for i in range(len(test_sets)):
        test_instance = test_sets[i]
        k_nearest_sets = get_k_neighbors(train_sets, test_instance, k)
        label_result = label_predict(k_nearest_sets)
        print '>','real sets=', test_instance[-1], ';', 'predict sets=', label_result
        predict_sets.append(label_result)
    accuracy = get_accuracy(test_sets, predict_sets)
    print  accuracy

