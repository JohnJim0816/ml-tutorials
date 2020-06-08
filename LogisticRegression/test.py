#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-06-06 17:48:13
@LastEditor: John
@LastEditTime: 2020-06-09 00:57:06
@Discription: 
@Environment: python 3.7.7
'''
import numpy as np
import os 
import sys

x=np.mat(1.2*np.ones(4))
np.save(os.path.dirname(sys.argv[0])+"/theta.npy",x)
theta=np.mat(1*np.ones(4))
y=np.dot(x,theta.T)
er=1-y
if er[0]==-3.8:print(er[0]==-3.8)


grad = 1*x
print(grad)
theta+= 1.1*grad
print(theta)
print(np.dot(x,theta.T))


