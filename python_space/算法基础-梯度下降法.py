# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：算法基础-梯度下降法
"""

# 导入模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import numpy as np
import matplotlib.pyplot as plt

# ######################################################################################################################
''' 已知损失函数，计算梯度下降 '''
# https://www.cnblogs.com/freeman818/p/8039971.html
# ######################################################################################################################

# 生成测试数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 生成序列X ,在-1到6直接产生140个点
plot_x = np.linspace(-1,6,141)

# 生成序列Y， 二次函数
plot_y = (plot_x-2.5)**2 - 1

# 绘制二次函数图像
plt.plot(plot_x, plot_y)
plt.show()

# 梯度下降法，代码封装~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 写出损失函数
# f(x) = y = (x-2.5)**2 -1

# 查看不同初始值，不同学习率情况下，梯度下降情况，特殊情况：当学习率过大时，会报错，后面会进行优化。
def grad_desc(initial_theta, eta, epsilon=1e-8):

    # 定义初始参数：参数初始值，参数历史值存储列表
    theta = initial_theta
    theta_history = [initial_theta]

    # 定义损失函数，计算损失函数的梯度
    def DJ(theta):
        grad_f = 2 * (theta - 2.5)
        return grad_f

    # 计算theta对应的损失函数值
    def J(theta):
        f_theta = (theta - 2.5) ** 2 - 1
        return f_theta

    # 实现梯度下降法
    while True:
        gradient = DJ(theta=theta)
        last_theta = theta
        theta = theta - eta * gradient
        theta_history.append(theta)

        if (abs(J(theta=theta) - J(theta=last_theta)) < epsilon):
            break

    return {'theta': theta, 'theta_history': theta_history}

# 绘制梯度下降的过程图像
def plot_theta_history(plot_x, theta_history):

    import numpy as np
    import matplotlib.pyplot as plt

    # 计算theta对应的损失函数值
    def J(theta):
        f_theta = (theta - 2.5) ** 2 - 1
        return f_theta

    # 绘制损失函数变化图
    plt.plot(plot_x, J(theta=plot_x))
    plt.plot(np.array(theta_history), J(theta=np.array(theta_history)), color='red', marker='+')
    plt.show()

# 梯度下降算法实现
result = grad_desc(initial_theta=0.0, eta=0.1)
plot_theta_history(plot_x, result['theta_history'])

# 梯度下降法，代码封装优化~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 优化问题：如果学习率过大，会报错toolager，进行判断，如果过大，返回inf。   新增加参数： 最大迭代次数。

def grad_desc(initial_theta, eta, n_iters=1000, epsilon=1e-8):

    # 初始化参数：参数，参数历史列表，最大迭代次数，初始迭代次数。
    theta = initial_theta
    theta_history = [initial_theta]
    n_iters = n_iters
    i_iters = 0

    # 定义损失函数：计算损失函数的梯度
    def DJ(theta):
        grad_f = 2 * (theta - 2.5)
        return grad_f

    # 计算theta对应的损失函数值
    def J(theta):
        # 如果学习率过大，会报错toolager，进行判断，如果过大，返回inf
        try:
            f_theta = (theta - 2.5) ** 2 - 1
            return f_theta
        except:
            return float('inf')

    # 实现梯度下降法
    while i_iters < n_iters:
        gradient = DJ(theta=theta)
        last_theta = theta
        theta = theta - eta * gradient
        theta_history.append(theta)

        if (abs(J(theta=theta) - J(theta=last_theta)) < epsilon):
            break
        i_iters += 1

    # 返回函数值
    return {'theta': theta, 'theta_history': theta_history}

# 梯度下降算法实现
result = grad_desc(initial_theta = 0.0, eta=1.1,n_iters= 10)
plot_theta_history(plot_x, result['theta_history'])

# ######################################################################################################################
''' 利用梯度下降，求解一元线性回归模型 '''
# https://www.cnblogs.com/freeman818/p/8039971.html
# ######################################################################################################################

# 生成随机数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
np.random.seed(1234)
x = 2 * np.random.random(size=100)
y = x * 3. + 4. + np.random.normal(size=100)

plt.scatter(x, y)
plt.show()

# 梯度下降法，求解线性回归模型~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 损失函数：J(theta)=MSE(y,y~)
# 目标：使得损失函数值最小
# 梯度：损失函数在参数theta处的对应的梯度

def grad_desc(X_b, Y, initial_theta, eta, n_iters=1000, epsilon=1e-8):

    # 初始化参数：参数（序列，两个参数），初始迭代次数。
    theta = initial_theta
    i_iters = 0

    # 损失函数值计算：计算参数theta处对应的损失函数值
    def J(X_b, Y, theta):
        try:
            return np.sum((Y - X_b.dot(theta)) ** 2) / len(X_b)
        except:
            return float('inf')  # 如果toolage，返回一个最大值。

    # 损失函数梯度计算：计算参数theta处对应的梯度（一元对应的为导数）
    def DJ(X_b, Y, theta):
        res = np.empty(len(theta))
        res[0] = np.sum(X_b.dot(theta) - Y)
        for i in range(1, len(theta)):
            res[i] = (X_b.dot(theta) - Y).dot(X_b[:, i])  # 少了np.sum
        return res * 2 / len(X_b)

    # 梯度下降法实现。
    while i_iters < n_iters:
        gradient = DJ(X_b, Y, theta)
        last_theta = theta
        theta = theta - eta * gradient

        if (abs(J(X_b, Y, theta) - J(X_b, Y, last_theta)) < epsilon):
            break
        i_iters += 1

    # 返回最终参数
    return {'theta': theta}

# 利用随机梯度下降实现一元线性回归模型~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
X_b = np.hstack([np.ones((len(x), 1)), x.reshape(-1,1)])
initial_theta = np.zeros(X_b.shape[1])
eta = 0.01

grad_desc(X_b=X_b, Y=y, initial_theta=initial_theta, eta=eta,n_iters= 1000, epsilon=1e-8)

