# -*- coding:utf-8 -*-
import numpy as np

numbers = np.array([1,2,3,4])
print(numbers.dtype)

numbers2 = np.array([1,2,3,4.0])
print(numbers2.dtype)

"""数据类型"""
numbers3 = np.array([1,2,3,'4'])
print(numbers3.dtype)

"""逻辑判断"""
vector = np.array([5,10,15,20])
print(vector == 10)

print('与运算结果',(vector == 10) & (vector == 5))
print('或运算结果',(vector == 10) | (vector == 5))

"""类型转换"""
vector = np.array(['1','2','3','4'])
print('转换前的数据类型',vector.dtype)
vector = vector.astype('float')
print('转换后的数据类型',vector.dtype)

vector = np.array([[5,10,15],[20,25,30],[35,40,45]])
print('最大值：',vector.max())
print('最小值：',vector.min())

#  求和，
# print(vector)
print(vector.sum())
print(vector.sum(axis=1))  # 按行求和
print(vector.sum(axis=0))  # 按列求和

# 一维数组转换为二维数组
a = np.array([1,2,3,4]) # 或者 a = np.arange(5)
print('shape of a:',a.shape)
print('reshape a:',a.reshape(-1,1).shape)

# 矩阵的属性,shape ,dtype, ndim, size
print('shape:',a.shape,'dtype:',a.dtype,'ndim:',a.ndim,'size:',a.size)

# 初始化特殊的矩阵
ar = np.zeros((3,4)) # 全0矩阵
print(ar)
ar = np.ones((3,4),dtype=int)  # 初始化全1矩阵
print(ar)

# print(np.arange(10,30,5).reshape((2,2)))

# 随机
print(np.random.random(5))

# 矩阵的乘法
a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])
print('a',a)
print('--------------')
print('b',b)
print('--------------')
print(a*b)  # 矩阵对应位置元素相乘
print('--------------')
print(a.dot(b))  # 矩阵的乘法，mxn , nxp  = mxp,或者np.dot(a,b)

# e的n次方
# b = np.exp(np.arange(4))
# print(b)

# 开根号
# c = np.sqrt(np.array([1,4,9,16,25]))
# print(c)

# print(np.floor(10*np.random.random((3,4)))

a = 10*np.random.random((3,4))
print(a)
a1 = np.floor(a)
print(a1)
print(a.ravel())  # 把矩阵转换为一维矩阵，flattern

a1.shape = (6,2)  # 修改矩阵的形状
print(a1)
print(a1.T)  # 矩阵的转置

"""矩阵的拼接"""
a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))
print(a)
print('--------')
print(b)
print('----hstack----')
print(np.hstack((a,b)))
print('---vstack-----')
print(np.vstack((a,b)))

"""矩阵的拆分"""
a = np.floor(10*np.random.random((2,12)))
print(a)
print('---------')
print(np.hsplit(a,3)[0])
print('-----')
print(np.hsplit(a,3)[1])
print('-----')
print(np.hsplit(a,3)[2])

print('-----vsplit-------')
a = a.reshape((12,2))
print(a)
print('-------')
print(np.vsplit(a,2)[0])
print('-------')
print(np.vsplit(a,2)[0])


print("-----复制的问题-----")
a = np.arange(12)
b = a
print(b is a)
b.shape = (3,4)
print(id(a))
print(id(b))

# 深复制，指向不同的内存区域
a = np.arange(12)
c = a.copy()
c[0] = 11
print(a,c,sep='\n')
print('id(a):',id(a),'id(c):',id(c))
print('c is a?:',c is a)

"""np.tile数组快速扩展"""
a = np.arange(0,40,10)
print(a)
b = np.tile(a,(2,2))
print(b,b.shape,sep='\n')

"""数组排序"""
a = np.array([[4,3,5],[1,2,1]])
print(a)
b = np.sort(a, axis=1)
print('--sort b---')
print(b)
print('--------')
a1 = np.array([4,3,1,2])
c = np.argsort(a1)
print(c)
print(a1[c])

