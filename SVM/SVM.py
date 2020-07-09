#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-07-09 15:01:26
@LastEditor: John
@LastEditTime: 2020-07-09 15:13:40
@Discription: 
@Environment: python 3.7.7
'''
# 导入处于不同目录下的Mnist.load_data
import os 
import sys
parent_path=os.path.dirname(os.path.dirname(sys.argv[0])) # 获取上级目录
sys.path.append(parent_path) # 修改sys.path
from Mnist.load_data import load_local_mnist
from sklearn import datasets, svm, metrics
from sklearn.metrics import classification_report


if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = load_local_mnist(one_hot=False)
    classifier = svm.SVC(C=200,kernel='rbf',gamma=0.01,cache_size=8000,probability=False) # 各系数说明：https://blog.csdn.net/qq_16953611/article/details/82414129
    classifier.fit(x_train, y_train)
    y_predicted = classifier.predict(x_test)
    target_names = ['class 1', 'class -1']
    print(classification_report(y_test, y_predicted, target_names=target_names))