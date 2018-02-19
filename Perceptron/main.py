'''
This program is used to show how Perceptron works on classification problems
Generate random fake data and use Perceptron to classify
'''
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt


def sign(x):
    if x >= 0:
        return 1
    else:
        return -1


# Generate Fake Data.
print('Randomly generate fake data.')
position_X = [np.float32(np.random.random() * 100) for i in range(100)]
position_Y = [np.float32(np.random.random() * 100) for i in range(100)]
print(position_X)
dataset = []
trainData, trainLabel = [], []
for i in range(100):
    if position_Y[i] >= position_X[i]:
        dataset.append((position_X[i], position_Y[i], -1))
        trainData.append((position_X[i], position_Y[i]))
        trainLabel.append(1)
        plt.plot(position_X[i], position_Y[i], 'ro')
    else:
        dataset.append((position_X[i], position_Y[i], 1))
        trainData.append((position_X[i], position_Y[i]))
        trainLabel.append(-1)
        plt.plot(position_X[i], position_Y[i], 'bo')
# TensorFlow Graph
trainingStep = 120
globalstep = tf.Variable(0)
learning_rate = tf.train.exponential_decay(
    0.2, globalstep, 10, 0.96, staircase=True)
x0 = 1
theta = tf.Variable(tf.random_uniform([3, 1]))
x = tf.placeholder('float', [None, 3])
bias = tf.Variable(tf.zeros([1]))
d = tf.abs((tf.matmul(x, theta)))
loss = tf.reduce_mean(d)
# Optimizer
train = tf.train.GradientDescentOptimizer(
    learning_rate).minimize(loss, global_step=globalstep)
init = tf.global_variables_initializer()
# Calculation
with tf.Session() as sess:
    sess.run(init)
    for j in range(trainingStep):
        wrong = []
        for i in range(len(trainData)):
            tx = sess.run(theta)[0] * 1 + sess.run(theta)[1] * \
                trainData[i][0] + sess.run(theta)[2] * trainData[i][1]
            if sign(tx) != trainLabel[i]:
                wrong.append([1, trainData[i][0], trainData[i][1]])
        if wrong == []:
            t = sess.run(theta)
            print(t, j)
            t0, t1, t2 = t[0], t[1], t[2]
            plt.plot([0, 100], [-t0 / t2, (-t1 / t2) * 100 - t0 / t2], 'k-')
            plt.show()
            exit()
        sess.run(train, feed_dict={x: wrong})
        if j % 10 == 0:
            print('step:{},loss:{}'.format(j, sess.run(
                loss, feed_dict={x: wrong})))
    t = sess.run(theta)
    print(t)
    t0, t1, t2 = t[0], t[1], t[2]
    plt.plot([0, 100], [-t0 / t2, (-t1 / t2) * 100 - t0 / t2], 'k-')
    plt.show()
