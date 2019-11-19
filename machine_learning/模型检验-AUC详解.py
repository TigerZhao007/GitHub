
# ######################################################################################################################
# AUC方法实现
# ######################################################################################################################

# 自己按照公式实现~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def auc_calculate(labels, preds, n_bins=100):

    postive_len = sum(labels)
    negative_len = len(labels) - postive_len
    total_case = postive_len * negative_len
    pos_histogram = [0 for _ in range(n_bins)]
    neg_histogram = [0 for _ in range(n_bins)]
    bin_width = 1.0 / n_bins
    for i in range(len(labels)):
        nth_bin = int(preds[i]/bin_width)
        if labels[i]==1:
            pos_histogram[nth_bin] += 1
        else:
            neg_histogram[nth_bin] += 1
    accumulated_neg = 0
    satisfied_pair = 0
    for i in range(n_bins):
        satisfied_pair += (pos_histogram[i]*accumulated_neg + pos_histogram[i]*neg_histogram[i]*0.5)
        accumulated_neg += neg_histogram[i]

    return satisfied_pair / float(total_case)

# 自定义函数与系统函数对比~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':

    import numpy as np
    from sklearn.metrics import roc_curve
    from sklearn.metrics import auc

    y = np.array([1, 0, 0, 0, 1, 0, 1, 0])
    pred = np.array([0.9, 0.8, 0.3, 0.1, 0.4, 0.9, 0.66, 0.7])

    fpr, tpr, thresholds = roc_curve(y, pred, pos_label=1)
    print("-----sklearn:", auc(fpr, tpr))
    print("-----py脚本:", auc_calculate(y, pred))

# ######################################################################################################################
# AUC方法介绍
# ######################################################################################################################

# AUC的理解~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUC就是：随机抽出一对样本（一个正样本，一个负样本），
# 然后用训练得到的分类器来对这两个样本进行预测，预测得到正样本的概率大于负样本概率的概率。

# AUC的优点~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 它不受类别不平衡问题的影响，不同的样本比例不会影响AUC的评测结果。
# 在训练时，可以直接使用AUC作为损失函数。

