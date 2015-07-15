#!/usr/bin/env python
#coding=utf8
'''
    @author: 段家公子
    @date: 2015-7-16
    @desc: use 40 points test svm kernel='linear'
'''

from sklearn import svm
import numpy as np
import pylab as pl

# random product 40 points
#seed里加上具体的数值相当于指定了随机产生的方法，每次运行此程序都是会产生同样的方法
np.random.seed(0)
'''
np.random.randn(4,2) 产生随机矩阵
[[ 1.76405235  0.40015721]
 [ 0.97873798  2.2408932 ]
  [ 1.86755799 -0.97727788]
   [ 0.95008842 -0.15135721]]
'''
# X产生了上下各20个点,Y produce two class label zero and one 
X = np.r_[np.random.randn(20,2)-[2,2], np.random.randn(20,2)+[2,2]]
Y = [0]*20 + [1]*20
print len(X)
print Y
#fit model
cls = svm.SVC(kernel = 'linear')
cls.fit(X, Y)
#get the separabel hyperplane 超平面
print dir(cls)
w = cls.coef_[0]
a = -w[0]/w[1]
xx = np.linspace(-5,5)
print len(xx)
yy = a*xx - (cls.intercept_[0])/w[1]
#np.linspace(-5, 5): -5 到5之间数值的list

# get up and down
b = cls.support_vectors_[0]
yy_down = a*xx + (b[1] - a*b[0])
b = cls.support_vectors_[-1]
yy_up = a*xx + (b[1] - a*b[0])

print 'w:', w
print 'a:', a

#plot
pl.plot(xx, yy, 'k-')
pl.plot(xx, yy_down, 'k--')
pl.plot(xx, yy_up, 'k--')

# draw points
pl.scatter(cls.support_vectors_[:, 0], cls.support_vectors_[:, 1], s = 80, facecolors='none')
pl.scatter(X[:,0], X[:,1], c=Y, cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()
