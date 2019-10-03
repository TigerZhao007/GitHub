
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)
x = 2 * np.random.random(size=100)
y = x * 3. + 4. + np.random.normal(size=100)

plt.scatter(x, y)
plt.show()

### 使用梯度下降法训练

### 损失函数：J(theta)=MSE(y,y~)
### 目标：使得损失函数值最小
### 梯度：损失函数在参数theta处的对应的梯度

# 计算参数theta处对应的损失函数值
def J( X_b, Y, theta):
    try:
        return np.sum((Y - X_b.dot(theta))**2) / len(X_b)
    except:
        return float('inf') # 如果toolage，返回一个最大值。

# J(X_b=X_b, Y=y, theta= initial_theta)

# 计算参数theta处对应的梯度（一元对应的为导数）
def DJ(X_b, Y, theta):
    res = np.empty(len(theta))
    res[0] = np.sum(X_b.dot(theta) - Y )
    for i in range(1, len(theta)):
        res[i] = (X_b.dot(theta) - Y).dot(X_b[:,i])    # 少了np.sum
    return res * 2 / len(X_b)

# DJ(X_b=X_b, Y=y, theta= initial_theta)

# ############################
# 梯度下降法，代码封装优化
# 优化问题：如果学习率过大，会报错toolager，进行判断，如果过大，返回inf
# 新增加参数： 最大迭代次数
def grad_desc(X_b, Y, initial_theta, eta, n_iters=1000, epsilon=1e-8):
    theta = initial_theta
    i_iters = 0

    # 实现梯度下降法
    while i_iters < n_iters:
        gradient = DJ(X_b, Y, theta)
        last_theta = theta
        theta = theta - eta * gradient

        if (abs(J(X_b, Y, theta) - J(X_b, Y, last_theta)) < epsilon):
            break
        i_iters += 1

    return {'theta': theta}

X_b = np.hstack([np.ones((len(x), 1)), x.reshape(-1,1)])
initial_theta = np.zeros(X_b.shape[1])
eta = 0.01

grad_desc(X_b=X_b, Y=y, initial_theta=initial_theta, eta=eta,n_iters= 1000, epsilon=1e-8)










