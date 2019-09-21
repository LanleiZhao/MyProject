# -*- coding:utf-8 -*-
""""
梯度下降BGD，随机梯度下降SGD，小批量梯度下降MBGD
"""
import random

def bgd():
    """
    梯度下降
    :return:
    """
    # 用y = Θ1*x1 + Θ2*x2来拟合下面的输入和输出
    # input1  1   2   5   4
    # input2  4   5   1   2
    # output  19  26  19  20
    input_x = [[1,4],[2,5],[5,1],[4,2]]
    y = [19,26,19,20]
    theta = [1,1]
    loss = 10
    step_size = 0.01
    eps = 0.0001
    max_iters = 10000
    error = 0
    iter_count = 0
    err1 = [0,0,0,0]
    err2 = [0,0,0,0]







if __name__ == '__main__':
    bgd()
