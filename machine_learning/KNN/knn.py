#!/usr/bin/env python
#coding=utf8

from sklearn import neighbors
from sklearn import datasets

# neighbors is sub package
'''

three kinds: 'setosa', 'versicolor', 'virginica' 

'''

def main():
    #print dir(neighbors)
    #build models
    knn = neighbors.KNeighborsClassifier()
    #print dir(datasets)
    iris = datasets.load_iris()
    print '\n\n'
    print iris

    print dir(knn)
    knn.fit(iris.data, iris.target)
    predit_label = knn.predict([[0.1, 0.2, 0.3, 0.4]])
    print predit_label

'''
predit_label-->0: 表示预测的结果是第一类：即setosa class

'''



if __name__ == '__main__':
    main()
