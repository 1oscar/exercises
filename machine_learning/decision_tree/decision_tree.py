#!/usr/bin/env python
#coding=utf8

import csv

from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree


def handler():
    #hander file
    content = open('./decision_tree_datasets.csv', 'r')
    reader = csv.reader(content)
    print dir(reader)
    
    headers = reader.next()
    #print headers
    '''
    with open('./decision_tree_datasets.csv', 'r') as f:
        reader = csv.reader(f)
        print reader.next()
    '''
    #handle list
    feature_list = []
    label_list = []

    for row in reader:
        label_list.append(row[-1])
        feature_dict = {}
        for i in range(1, len(headers)-1):
            feature_dict[headers[i]] = row[i]
        feature_list.append(feature_dict)
    print feature_list
    print 'dkf\t'*5
    print label_list

    #vectorize feature ==> vertor [1, 0, 0, ...]
    #print dir(DictVectorizer)
    vec = DictVectorizer()
    print dir(vec)
    dummy_x = vec.fit_transform(feature_list).toarray()
    print dummy_x
    #以字母顺序排序
    print vec.get_feature_names()
    
    #vectorize class label
    print dir(preprocessing)
    lb= preprocessing.LabelBinarizer()
    print dir(lb)
    dummy_y = lb.fit_transform(label_list)
    print str(dummy_y)

    #decision tree algorithms
    print dir(tree)
    # criterion entropy use ID3 algorithms
    decision_tree = tree.DecisionTreeClassifier(criterion = 'entropy')
    #print dir(tree.DecisionTreeClassifier)
    result = decision_tree.fit(dummy_x, dummy_y)
    #result is model named decision tree by trained
    print result
    
    # draw decision tree
    print dir(tree)
    
    '''
    with open('./result.dot', 'w') as f:
        f = tree.export_graphviz(result, feature_names = vec.get_feature_names(), out_file = f)
    '''
    # random extract one line
    one_row_x = dummy_x[0, :]
    print one_row_x

    new_row = one_row_x
    new_row[0] = 1
    new_row[2] = 0
    print new_row

    #one line predict result
    print dir(result)
    predict_result = result.predict(new_row)
    print predict_result
    

if __name__ == '__main__':
    handler()
