---
title: "决策树"
tags: [python, scikit-learn]
---

### 用途： 银行信息自动评估系统; 商家用户行为分析
#### 代码说明

1. [**CSV datasets**](https://github.com/1oscar/exercises/blob/master/machine_learning/decision_tree/decision_tree_datasets.csv)
2. ` headers = reader.next()` :表示 **['RID', 'age', 'income', 'student', 'credit_rating', 'class_buys_computer']**
3. 特征值和类标记分别用列表存储
4. 类标记：**['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']**, 特征值列表里存储字典，每个字典代表一个样本实例的feature，dict里k表示headers里的值，v指的是对应headers值的值
5. `from sklearn.feature_extraction import DictVectorizer`
6. `vec.fit_transform(feature_list).toarray()`将`feature_list`转换为数组（多维）
7. `from sklearn import preprocessing`
8. `preprocessing.LabelBinarizer().fit_transform(label_list)`处理`label_list`
9. `from sklearn import tree` 决策树
10. `result = tree.DecisionTreeClassifier(criterion = 'entropy')..fit(dummy_x, dummy_y)` : result 表示训练出来的算法模型， criterion 不写，默认时gini准则，这里用的是ID3算法，准则用的是熵
11. `result.predict(new_row)` 表示预测新的样本，得出预测的结果
12. 决策树导出图形保存到f中

 ```python
 with open('./result.dot', 'w') as f:
     tree.export_graphviz(result, feature_names = vec.get_feature_names(), out_file = f) 
 ```
13. 讲`dot`文件保存为`pdf`文件： `mac`命令行下： `dot -Tpdf result.pdf -o result.pdf`


