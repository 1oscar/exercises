---
title: "SVM算法"
tags: [python, scikit-learn]
---

### 用途： 图片中的红眼检测；结肠癌早晚期分类
#### 代码说明

1. `use_svm.png` 是使用`sklearn` 的小例子，预测`[2,0]`的分类
2. `use_svm_example.py`是随机产生40个点，用核函数`linear`来准确的对这个40个点分类
3. 随机产生四十个点 `np`
4. 建立模型`cls = svm.SVC(kernel='linear')` and `cls.fit(X,Y)` `etc.`
5. 得出超平面的函数`csl.coef_[0] ...`
6. 得出与超平面等距离的两条平面函数`yy_down` and `yy_up`
7. 画出三个平面`pl.plot(...)`
8. 描出点`pl.scatter(...)`
9. `pl.title(..)`内容有长度限制，由`utf8`-->`unicode`节省了占用空间
10. `pl.show()`才会最终显示`SVM`的分类图像
11. 图片![result](https://github.com/1oscar/exercises/blob/master/machine_learning/SVM/1.png)
