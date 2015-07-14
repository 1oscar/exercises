---
title: "最近邻算法"
tags: [python, scikit-learn]
---

### 用途： 人脸识别
#### 代码说明

1. `knn.py`: 针对`sklearn`中的最近邻居算法(`neighbors`)的使用
2. `knn_implementations.py` 是最近邻算法的实现环节
3. `load_file`按照 `split_criterion`来把数据集切分成测试数据集合，训练数据集合
4. `cal_distance`只计算两个实例样本之间的距离，这里使用`math.pow`or `pow` 是一样的
5. `get_k_neighbors`是得到训练数据集每个已知实例与未知实例`test_instance`的距离，返回距离列表里的k个最近的距离，即最小的距离
6. 排序的两种方式，`list.sort(key=operator.itemgetter(1))`or `list.sort(key=lambda x:x[1])`都是表示的按照list中第二个元素来排序,`reverse=True`可以指定，忽略就是默认生序，`True`就是降序
7. **`label_predict`依据输入的k个最近邻已知实例的样本，判断K个实例里面`label`最多的是那个`label class`, 定义地点，用 `reponse` `store label class`, 判断`reponse`是否在字典里，在，`value`个数加1，否则，字典添加`reponse`, 赋值为为1**
8. **字典`k`为`label class`，`V` `is` `count`,按照`V`降序排列，使用`sorted`,sorted(countd_dict.iteritems(), key=lambda x:x[1], reverse=True), 返回值是一个列表，列表里是元组对，`K and V` 的元组对**
9. `get_accuracy`得到测试集里真实的`label class `和预测出来的`label`是否一致，得出准确率