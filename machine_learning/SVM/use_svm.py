#!/usr/bin/env python
#coding=utf8
'''
    @author: 段家公子
    @date: 2015-7-15
    @desc: 使用sklearn.svm的例子
'''

from sklearn import svm 



def test():
    x = [[1,1], [2,0], [2,3]]
    # y is class label, here is two class label zero and one
    y = [0, 0, 1]
    #fit svm model
    #SVC default is rbf:径向基核函数
    #It must be one of 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'
    cls = svm.SVC(kernel='linear')
    #print dir(cls)
    cls.fit(x, y)
    print cls
    print dir(cls)
    #Support vectors.
    print cls.support_vectors_
    # Indices of support vectors.
    print cls.support_
    #Number of support vectors for each class.
    print cls.n_support_
    #predict
    print cls.predict([2,0])


if __name__ == '__main__':
    test()


