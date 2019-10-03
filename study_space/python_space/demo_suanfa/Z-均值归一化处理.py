import numpy as np

# ############################
# 归一化feature
# https://www.cnblogs.com/freeman818/p/8039971.html
# ############################
def featureNormaliza(X):
    X_norm = np.array(X)  # 将X转化为numpy数组对象，才可以进行矩阵的运算
    # 定义所需变量
    mu = np.zeros((1, X.shape[1]))
    sigma = np.zeros((1, X.shape[1]))

    mu = np.mean(X_norm, 0)  # 求每一列的平均值（0指定为列，1代表行）
    sigma = np.std(X_norm, 0)  # 求每一列的标准差
    for i in range(X.shape[1]):  # 遍历列
        X_norm[:, i] = (X_norm[:, i] - mu[i]) / sigma[i]  # 归一化

    return X_norm, mu, sigma
