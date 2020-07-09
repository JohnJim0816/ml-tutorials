#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-06-30 20:35:26
@LastEditor: John
@LastEditTime: 2020-06-30 20:45:32
@Discription: 
@Environment: python 3.7.7
'''
from tqdm import tqdm
from time import sleep

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    sleep(0.25)
    text = text + char