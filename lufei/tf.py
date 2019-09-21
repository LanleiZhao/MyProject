# -*- coding:utf-8 -*-
import tensorflow as tf

a = tf.constant(1.0)
b = tf.constant(2.0)
c = tf.add(a,b)

print(c)