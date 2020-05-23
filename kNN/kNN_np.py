#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-05-22 10:55:13
@LastEditor: John
@LastEditTime: 2020-05-22 21:06:33
@Discription: 
@Environment: python 3.7.7
'''
# 参考https://github.com/Dod-o/Statistical-Learning-Method_Code/blob/master/KNN/KNN.py
# kNN的大头在于向量的计算，考虑采用tensorflow

import time

if __name__ == "__main__":
    
    start = time.time()

    #获取训练集
    trainDataArr, trainLabelArr = loadData('../Mnist/mnist_train.csv')
    #获取测试集
    testDataArr, testLabelArr = loadData('../Mnist/mnist_test.csv')
    #计算测试集正确率
    accur = model_test(trainDataArr, trainLabelArr, testDataArr, testLabelArr, 25)
    #打印正确率
    print('accur is:%d'%(accur * 100), '%')

    end = time.time()
    #显示花费时间
    print('time span:', end - start)