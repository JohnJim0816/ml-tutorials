#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-05-22 07:46:13
@LastEditor: John
@LastEditTime: 2020-05-22 07:47:15
@Discription: 
@Environment: python 3.7.7
'''
from keras.datasets import mnist
from keras.utils import np_utils
import numpy as np


def load_data():  # categorical_crossentropy
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    number = 10000
    x_train, y_train = x_train[0:number], y_train[0:number]
    x_train = x_train.reshape(number, 28 * 28)
    x_test = x_test.reshape(x_test.shape[0], 28 * 28)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    # convert class vectors to binary class matrices
    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)
    x_test = np.random.normal(x_test)  # 加噪声

    x_train, x_test = x_train / 255, x_test / 255

    return (x_train, y_train), (x_test, y_test)


(x_train, y_train), (x_test, y_test) = load_data()
