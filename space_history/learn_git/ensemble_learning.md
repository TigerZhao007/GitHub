
# 集成学习算法学习笔记

# 一、集成学习算法总结
原文网址：http://www.cnblogs.com/pinard/p/6131423.html

集成学习(ensemble learning)可以说是现在非常火爆的机器学习方法了。
它本身不是一个单独的机器学习算法，而是通过构建并结合多个机器学习器来完成学习任务。
也就是我们常说的“博采众长”。<br>
集成学习可以用于分类问题集成，回归问题集成，特征选取集成，异常点检测集成等等，
可以说所有的机器学习领域都可以看到集成学习的身影。本文就对集成学习的原理做一个总结。<br>

## 1. 集成学习概述

对集成学习的思想做一个概括。对于训练集数据，我们通过训练若干个个体学习器，
通过一定的结合策略，就可以最终形成一个强学习器，以达到博采众长的目的。<br>
也就是说，集成学习有两个主要的问题需要解决，第一是如何得到若干个个体学习器，
第二是如何选择一种结合策略，将这些个体学习器集合成一个强学习器。<br>
![Alt text](https://images2015.cnblogs.com/blog/1042406/201612/1042406-20161204191919974-1029671964.png)

## 2. 集成学习之个体学习器
集成学习的第一个问题就是如何得到若干个个体学习器。这里我们有两种选择:<br>
第一种就是所有的个体学习器都是一个种类的，或者说是同质的。
比如都是决策树个体学习器，或者都是神经网络个体学习器。<br>
第二种是所有的个体学习器不全是一个种类的，或者说是异质的。
比如我们有一个分类问题，对训练集采用支持向量机个体学习器，逻辑回归个体学习器和朴素贝叶斯个体学习器来学习，
再通过某种结合策略来确定最终的分类强学习器。<br>

目前来说，同质个体学习器的应用是最广泛的，一般我们常说的集成学习的方法都是指的同质个体学习器。
而同质个体学习器使用最多的模型是CART决策树和神经网络。
同质个体学习器按照个体学习器之间是否存在依赖关系可以分为两类:<br>
第一个是个体学习器之间存在强依赖关系，一系列个体学习器基本都需要串行生成，代表算法是boosting系列算法;<br>
第二个是个体学习器之间不存在强依赖关系，一系列个体学习器可以并行生成，代表算法是bagging和随机森林（Random Forest）系列算法。
下面就分别对这两类算法做一个概括总结。<br>

## 3. 集成学习之boosting
boosting的算法原理我们可以用一张图做一个概括如下：
![Alt text](https://images2015.cnblogs.com/blog/1042406/201612/1042406-20161204194331365-2142863547.png)

从图中可以看出，Boosting算法的工作机制是首先从训练集用初始权重训练出一个弱学习器1，
根据弱学习的学习误差率表现来更新训练样本的权重，使得之前弱学习器1学习误差率高的训练样本点的权重变高，
使得这些误差率高的点在后面的弱学习器2中得到更多的重视。然后基于调整权重后的训练集来训练弱学习器2.，
如此重复进行，直到弱学习器数达到事先指定的数目T，最终将这T个弱学习器通过集合策略进行整合，得到最终的强学习器。

Boosting系列算法里最著名算法主要有AdaBoost算法和提升树(boosting tree)系列算法。
提升树系列算法里面应用最广泛的是梯度提升树(Gradient Boosting Tree)。
AdaBoost和提升树算法的原理在后面的文章中会专门来讲。

## 4. 集成学习之bagging
Bagging的算法原理和 boosting不同，它的弱学习器之间没有依赖关系，可以并行生成，我们可以用一张图做一个概括如下：
![Alt text](https://images2015.cnblogs.com/blog/1042406/201612/1042406-20161204200000787-1988863729.png)

从上图可以看出，bagging的个体弱学习器的训练集是通过随机采样得到的。通过T次的随机采样，我们就可以得到T个采样集，
对于这T个采样集，我们可以分别独立的训练出T个弱学习器，再对这T个弱学习器通过集合策略来得到最终的强学习器。

对于这里的随机采样有必要做进一步的介绍，这里一般采用的是自助采样法（Bootstap sampling）,即对于m个样本的原始训练集，
我们每次先随机采集一个样本放入采样集，接着把该样本放回，也就是说下次采样时该样本仍有可能被采集到，这样采集m次，
最终可以得到m个样本的采样集，由于是随机采样，这样每次的采样集是和原始训练集不同的，和其他采样集也是不同的，
这样得到多个不同的弱学习器。

随机森林是bagging的一个特化进阶版，所谓的特化是因为随机森林的弱学习器都是决策树。
所谓的进阶是随机森林在bagging的样本随机采样基础上，又加上了特征的随机选择，其基本思想没有脱离bagging的范畴。
bagging和随机森林算法的原理在后面的文章中会专门来讲。

## 5. 集成学习之结合策略
在上面几节里面我们主要关注于学习器，提到了学习器的结合策略但没有细讲，本节就对集成学习之结合策略做一个总结。
我们假定我得到的T个弱学习器是{h1,h2,...ht}
### 5.1 平均法
对于`数值类`的回归预测问题，通常使用的结合策略是平均法，也就是说，对于若干个弱学习器的输出进行平均得到最终的预测输出。

最简单的平均是算术平均，也就是说最终预测是: H(x)=1T∑1Thi(x)

如果每个个体学习器有一个权重w，则最终预测是: H(x)=∑i=1Twihi(x)<br>
其中wi是个体学习器hi的权重，通常有wi≥0,∑i=1Twi=1
### 5.2 投票法
对于`分类问题`的预测，我们通常使用的是投票法。假设我们的预测类别是{c1,c2,...cK},对于任意一个预测样本x，
我们的T个弱学习器的预测结果分别是(h1(x),h2(x)...hT(x))。

最简单的投票法是相对多数投票法，也就是我们常说的少数服从多数，也就是T个弱学习器的对样本x的预测结果中，
数量最多的类别ci为最终的分类类别。如果不止一个类别获得最高票，则随机选择一个做最终类别。

稍微复杂的投票法是绝对多数投票法，也就是我们常说的要票过半数。在相对多数投票法的基础上，不光要求获得最高票，
还要求票过半数。否则会拒绝预测。

更加复杂的是加权投票法，和加权平均法一样，每个弱学习器的分类票数要乘以一个权重，最终将各个类别的加权票数求和，
最大的值对应的类别为最终类别。

### 5.3 学习法
上两节的方法都是对弱学习器的结果做平均或者投票，相对比较简单，但是可能学习误差较大，于是就有了学习法这种方法，
对于学习法，代表方法是stacking，当使用stacking的结合策略时， 我们不是对弱学习器的结果做简单的逻辑处理，
而是再加上一层学习器，也就是说，我们将训练集弱学习器的学习结果作为输入，将训练集的输出作为输出，
重新训练一个学习器来得到最终结果。

在这种情况下，我们将弱学习器称为初级学习器，将用于结合的学习器称为次级学习器。
对于测试集，我们首先用初级学习器预测一次，得到次级学习器的输入样本，再用次级学习器预测一次，得到最终的预测结果。

# 二、集成学习之Adaboost算法原理小结
原文链接：http://www.cnblogs.com/pinard/p/6133937.html

在集成学习原理小结中，我们讲到了集成学习按照个体学习器之间是否存在依赖关系可以分为两类，
第一个是个体学习器之间存在强依赖关系，另一类是个体学习器之间不存在强依赖关系。
前者的代表算法就是是boosting系列算法。在boosting系列算法中， Adaboost是最著名的算法之一。
Adaboost既可以用作分类，也可以用作回归。本文就对Adaboost算法做一个总结。

## 1. 回顾boosting算法的基本原理
在集成学习原理小结中，我们已经讲到了boosting算法系列的基本思想，如下图：
![Alt text](https://images2015.cnblogs.com/blog/1042406/201612/1042406-20161204194331365-2142863547.png)

从图中可以看出，Boosting算法的工作机制是首先从训练集用初始权重训练出一个弱学习器1，
根据弱学习的学习误差率表现来更新训练样本的权重，使得之前弱学习器1学习误差率高的训练样本点的权重变高，
使得这些误差率高的点在后面的弱学习器2中得到更多的重视。然后基于调整权重后的训练集来训练弱学习器2.，
如此重复进行，直到弱学习器数达到事先指定的数目T，最终将这T个弱学习器通过集合策略进行整合，得到最终的强学习器。　

不过有几个具体的问题Boosting算法没有详细说明。
* 1）如何计算学习误差率e?
* 2）如何得到弱学习器权重系数α?
* 3）如何更新样本权重D?
* 4）使用何种结合策略？

只要是boosting大家族的算法，都要解决这4个问题。那么Adaboost是怎么解决的呢？

## 2. Adaboost算法的基本思路
我们这里讲解Adaboost是如何解决上一节这4个问题的。
假设我们的训练集样本是<br>
T=\{(x_,y_1),(x_2,y_2), ...(x_m,y_m)\}

训练集的在第k个弱学习器的输出权重为<br>
D(k) = (w_{k1}, w_{k2}, ...w_{km}) ;\;\; w_{1i}=\frac{1}{m};\;\; i =1,2...m

首先我们看看Adaboost的分类问题。<br>
分类问题的误差率很好理解和计算。由于多元分类是二元分类的推广，这里假设我们是二元分类问题，输出为{-1，1}，
则第k个弱分类器G_k(x)在训练集上的加权误差率为<br>
e_k = P(G_k(x_i) \neq y_i) = \sum\limits_{i=1}^{m}w_{ki}I(G_k(x_i) \neq y_i)

接着我们看弱学习器权重系数,对于二元分类问题，第k个弱分类器G_k(x)的权重系数为<br>
\alpha_k = \frac{1}{2}log\frac{1-e_k}{e_k}

为什么这样计算弱学习器权重系数？从上式可以看出，如果分类误差率e_k越大，则对应的弱分类器权重系数\alpha_k越小。
也就是说，误差率小的弱分类器权重系数越大。具体为什么采用这个权重系数公式，我们在讲Adaboost的损失函数优化时再讲。

第三个问题，更新更新样本权重D。<br>
假设第k个弱分类器的样本集权重系数为:<br>
D(k) = (w_{k1}, w_{k2}, ...w_{km})

则对应的第k+1个弱分类器的样本集权重系数为<br>
w_{k+1,i} = \frac{w_{ki}}{Z_K}exp(-\alpha_ky_iG_k(x_i))

这里Z_k是规范化因子<br>
Z_k = \sum\limits_{i=1}^{m}w_{ki}exp(-\alpha_ky_iG_k(x_i))

从w_{k+1,i}计算公式可以看出，如果第i个样本分类错误，则y_iG_k(x_i) < 0，导致样本的权重在第k+1个弱分类器中增大，
如果分类正确，则权重在第k+1个弱分类器中减少.具体为什么采用样本权重更新公式，我们在讲Adaboost的损失函数优化时再讲。<br>

最后一个问题是集合策略。Adaboost分类采用的是加权表决法，最终的强分类器为<br>
f(x) = sign(\sum\limits_{k=1}^{K}\alpha_kG_k(x))　　　　

接着我们看看Adaboost的回归问题。由于Adaboost的回归问题有很多变种，这里我们以Adaboost R2算法为准。<br>

我们先看看回归问题的误差率的问题，对于第k个弱学习器，计算他在训练集上的最大误差<br>
E_k= max|y_i - G_k(x_i)|\;i=1,2...m

然后计算每个样本的相对误差<br>
e_{ki}= \frac{|y_i - G_k(x_i)|}{E_k}

这里是误差损失为线性时的情况，如果我们用平方误差，则e_{ki}= \frac{(y_i - G_k(x_i))^2}{E_k^2},如果我们用的是指数误差，
则e_{ki}= 1 - exp（\frac{-y_i + G_k(x_i))}{E_k}）

最终得到第k个弱学习器的 误差率<br>
e_k =  \sum\limits_{i=1}^{m}w_{ki}e_{ki}

我们再来看看如何得到弱学习器权重系数\alpha。这里有：<br>
\alpha_k =\frac{e_k}{1-e_k}

对于更新更新样本权重D，第k+1个弱学习器的样本集权重系数为<br>
w_{k+1,i} = \frac{w_{ki}}{Z_k}\alpha_k^{1-e_{ki}}

这里Z_k是规范化因子<br>
Z_k = \sum\limits_{i=1}^{m}w_{ki}\alpha_k^{1-e_{ki}}

最后是结合策略，和分类问题稍有不同，采用的是对加权的弱学习器取中位数的方法，最终的强回归器为<br>
f(x) = \sum\limits_{k=1}^{K}(ln\frac{1}{\alpha_k})g(x)<br>
其中，g(x)是所有\alpha_kG_k(x), k=1,2,....K的中位数。　

## 3. AdaBoost分类问题的损失函数优化
刚才上一节我们讲到了分类Adaboost的弱学习器权重系数公式和样本权重更新公式。但是没有解释选择这个公式的原因，
让人觉得是魔法公式一样。其实它可以从Adaboost的损失函数推导出来。

从另一个角度讲，　Adaboost是模型为加法模型，学习算法为前向分步学习算法，损失函数为指数函数的分类问题。

模型为加法模型好理解，我们的最终的强分类器是若干个弱分类器加权平均而得到的。

前向分步学习算法也好理解，我们的算法是通过一轮轮的弱学习器学习，利用前一个弱学习器的结果来更新后一个弱学习器的训练集权重。
也就是说，第k-1轮的强学习器为<br>
f_{k-1}(x) = \sum\limits_{i=1}^{k-1}\alpha_iG_{i}(x)<br>

而第k轮的强学习器为<br>
f_{k}(x) = \sum\limits_{i=1}^{k}\alpha_iG_{i}(x)

上两式一比较可以得到<br>
f_{k}(x) = f_{k-1}(x) + \alpha_kG_k(x)

可见强学习器的确是通过前向分步学习算法一步步而得到的。

Adaboost损失函数为指数函数，即定义损失函数为<br>
\underbrace{arg\;min\;}_{\alpha, G} \sum\limits_{i=1}^{m}exp(-y_if_{k}(x))

利用前向分步学习算法的关系可以得到损失函数为<br>
(\alpha_k, G_k(x)) = \underbrace{arg\;min\;}_{\alpha, G}\sum\limits_{i=1}^{m}exp[(-y_i) (f_{k-1}(x) + \alpha G(x))]<br>
令w_{ki}^{’} = exp(-y_if_{k-1}(x)), 它的值不依赖于\alpha, G,因此与最小化无关，仅仅依赖于f_{k-1}(x),随着每一轮迭代而改变。

将这个式子带入损失函数,损失函数转化为<br>
(\alpha_k, G_k(x)) = \underbrace{arg\;min\;}_{\alpha, G}\sum\limits_{i=1}^{m}w_{ki}^{’}exp[-y_i\alpha G(x)]
　　　　
首先，我们求G_k(x).，可以得到<br>
G_k(x) = \underbrace{arg\;min\;}_{G}\sum\limits_{i=1}^{m}w_{ki}^{’}I(y_i \neq G(x_i))<br>
将G_k(x)带入损失函数，并对\alpha求导，使其等于0，则就得到了<br>
\alpha_k = \frac{1}{2}log\frac{1-e_k}{e_k}<br>
其中，e_k即为我们前面的分类误差率。<br>
e_k = \frac{\sum\limits_{i=1}^{m}w_{ki}^{’}I(y_i \neq G(x_i))}{\sum\limits_{i=1}^{m}w_{ki}^{’}} = \sum\limits_{i=1}^{m}w_{ki}I(y_i \neq G(x_i))

最后看样本权重的更新。利用f_{k}(x) = f_{k-1}(x) + \alpha_kG_k(x)和w_{ki}^{’} = exp(-y_if_{k-1}(x))，即可得：<br>
w_{k+1,i}^{’} = w_{ki}^{’}exp[-y_i\alpha_kG_k(x)]

这样就得到了我们第二节的样本权重更新公式。

## 4. AdaBoost二元分类问题算法流程
这里我们对AdaBoost二元分类问题算法流程做一个总结。

`输入`为样本集T=\{(x_,y_1),(x_2,y_2), ...(x_m,y_m)\}，输出为{-1, +1}，弱分类器算法, 弱分类器迭代次数K。<br>
`输出`为最终的强分类器f(x)<br>

### 1) 初始化样本集权重为
D(1) = (w_{11}, w_{12}, ...w_{1m}) ;\;\; w_{1i}=\frac{1}{m};\;\; i =1,2...m
### 2) 对于k=1,2，...K:
* a) 使用具有权重D_k的样本集来训练数据，得到弱分类器G_k(x)<br>
* b)计算G_k(x)的分类误差率<br>
e_k = P(G_k(x_i) \neq y_i) = \sum\limits_{i=1}^{m}w_{ki}I(G_k(x_i) \neq y_i)<br>
* c) 计算弱分类器的系数<br>
\alpha_k = \frac{1}{2}log\frac{1-e_k}{e_k}<br>
* d) 更新样本集的权重分布
w_{k+1,i} = \frac{w_{ki}}{Z_K}exp(-\alpha_ky_iG_k(x_i)) \;\; i =1,2,...m<br>
这里Z_k是规范化因子<br>
Z_k = \sum\limits_{i=1}^{m}w_{ki}exp(-\alpha_ky_iG_k(x_i))<br>
### 3) 构建最终分类器为：
f(x) = sign(\sum\limits_{k=1}^{K}\alpha_kG_k(x))
　　　　
对于Adaboost多元分类算法，其实原理和二元分类类似，最主要区别在弱分类器的系数上。比如Adaboost SAMME算法，它的弱分类器的系数<br>
\alpha_k = \frac{1}{2}log\frac{1-e_k}{e_k} + log(R-1)<br>
其中R为类别数。从上式可以看出，如果是二元分类，R=2，则上式和我们的二元分类算法中的弱分类器的系数一致。

## 5. Adaboost回归问题的算法流程
这里我们对AdaBoost回归问题算法流程做一个总结。AdaBoost回归算法变种很多，下面的算法为Adaboost R2回归算法过程。

`输入`为样本集T=\{(x_,y_1),(x_2,y_2), ...(x_m,y_m)\}，，弱学习器算法, 弱学习器迭代次数K。<br>
`输出`为最终的强学习器f(x)<br>

### 1) 初始化样本集权重为
D(1) = (w_{11}, w_{12}, ...w_{1m}) ;\;\; w_{1i}=\frac{1}{m};\;\; i =1,2...m

### 2) 对于k=1,2，...K:
* a) 使用具有权重D_k的样本集来训练数据，得到弱学习器G_k(x)<br>
* b) 计算训练集上的最大误差<br>
E_k= max|y_i - G_k(x_i)|\;i=1,2...m<br>
* c) 计算每个样本的相对误差:<br>
>>如果是线性误差，则e_{ki}= \frac{|y_i - G_k(x_i)|}{E_k}；<br>
>>如果是平方误差，则e_{ki}= \frac{(y_i - G_k(x_i))^2}{E_k^2}<br>
>>如果是指数误差，则e_{ki}= 1 - exp（\frac{-|y_i -G_k(x_i)|}{E_k}）<br>　　　　　　　
* d) 计算回归误差率<br>
e_k =  \sum\limits_{i=1}^{m}w_{ki}e_{ki}<br>
* c) 计算弱学习器的系数<br>
\alpha_k =\frac{e_k}{1-e_k}
* d) 更新样本集的权重分布为
w_{k+1,i} = \frac{w_{ki}}{Z_k}\alpha_k^{1-e_{ki}}<br>
这里Z_k是规范化因子<br>
Z_k = \sum\limits_{i=1}^{m}w_{ki}\alpha_k^{1-e_{ki}}<br>
### 3) 构建最终强学习器为：
f(x) = \sum\limits_{k=1}^{K}(ln\frac{1}{\alpha_k})g(x)<br>
其中，g(x)是所有\alpha_kG_k(x), k=1,2,....K的中位数。<br>　　　

## 6. Adaboost算法的正则化
为了防止Adaboost过拟合，我们通常也会加入正则化项，这个正则化项我们通常称为步长(learning rate)。
定义为\nu,对于前面的弱学习器的迭代<br>
f_{k}(x) = f_{k-1}(x) + \alpha_kG_k(x)

如果我们加上了正则化项，则有<br>
f_{k}(x) = f_{k-1}(x) + \nu\alpha_kG_k(x)<br>
\nu的取值范围为0 < \nu \leq 1。<br>
对于同样的训练集学习效果，较小的\nu意味着我们需要更多的弱学习器的迭代次数。
通常我们用步长和迭代最大次数一起来决定算法的拟合效果。

## 7. Adaboost小结
到这里Adaboost就写完了，前面有一个没有提到，就是弱学习器的类型。理论上任何学习器都可以用于Adaboost.
但一般来说，使用最广泛的Adaboost弱学习器是决策树和神经网络。对于决策树，Adaboost分类用了CART分类树，
而Adaboost回归用了CART回归树。<br>
这里对Adaboost算法的优缺点做一个总结。

Adaboost的主要优点有：
* 1）Adaboost作为分类器时，分类精度很高
* 2）在Adaboost的框架下，可以使用各种回归分类模型来构建弱学习器，非常灵活。
* 3）作为简单的二元分类器时，构造简单，结果可理解。
* 4）不容易发生过拟合

Adaboost的主要缺点有：
1）对异常样本敏感，异常样本在迭代中可能会获得较高的权重，影响最终的强学习器的预测准确性。


# 三、Bagging与随机森林算法原理小结 
原文链接：https://www.cnblogs.com/pinard/p/6156009.html

在集成学习原理小结中，我们讲到了集成学习有两个流派，一个是boosting派系，它的特点是各个弱学习器之间有依赖关系。
另一种是bagging流派，它的特点是各个弱学习器之间没有依赖关系，可以并行拟合。
本文就对集成学习中Bagging与随机森林算法做一个总结。

随机森林是集成学习中可以和梯度提升树GBDT分庭抗礼的算法，尤其是它可以很方便的并行训练，
在如今大数据大样本的的时代很有诱惑力。

## 1.  bagging的原理
在集成学习原理小结中，我们给Bagging画了下面一张原理图。
![Alt text](https://images2015.cnblogs.com/blog/1042406/201612/1042406-20161204200000787-1988863729.png)

从上图可以看出，Bagging的弱学习器之间的确没有boosting那样的联系。它的特点在“随机采样”。那么什么是随机采样？

随机采样(bootsrap)就是从我们的训练集里面采集固定个数的样本，但是每采集一个样本后，都将样本放回。
也就是说，之前采集到的样本在放回后有可能继续被采集到。对于我们的Bagging算法，
一般会随机采集和训练集样本数m一样个数的样本。这样得到的采样集和训练集样本的个数相同，
但是样本内容不同。如果我们对有m个样本训练集做T次的随机采样，，则由于随机性，T个采样集各不相同。

注意到这和GBDT的子采样是不同的。GBDT的子采样是无放回采样，而Bagging的子采样是放回采样。

对于一个样本，它在某一次含m个样本的训练集的随机采样中，每次被采集到的概率是1m。不被采集到的概率为1?1m。
如果m次采样都没有被采集中的概率是(1?1m)m。当m→∞时，(1?1m)m→1e?0.368。
也就是说，在bagging的每轮随机采样中，训练集中大约有36.8%的数据没有被采样集采集中。

对于这部分大约36.8%的没有被采样到的数据，我们常常称之为袋外数据(Out Of Bag, 简称OOB)。
这些数据没有参与训练集模型的拟合，因此可以用来检测模型的泛化能力。

bagging对于弱学习器没有限制，这和Adaboost一样。但是最常用的一般也是决策树和神经网络。

bagging的集合策略也比较简单，对于分类问题，通常使用简单投票法，得到最多票数的类别或者类别之一为最终的模型输出。
对于回归问题，通常使用简单平均法，对T个弱学习器得到的回归结果进行算术平均得到最终的模型输出。

由于Bagging算法每次都进行采样来训练模型，因此泛化能力很强，对于降低模型的方差很有作用。
当然对于训练集的拟合程度就会差一些，也就是模型的偏倚会大一些。

## 2.  bagging算法流程

上一节我们对bagging算法的原理做了总结，这里就对bagging算法的流程做一个总结。相对于Boosting系列的Adaboost和GBDT，
bagging算法要简单的多。

输入为样本集D={(x,y1),(x2,y2),...(xm,ym)}，弱学习器算法, 弱分类器迭代次数T。<br>
输出为最终的强分类器f(x)<br>

* 1）对于t=1,2...,T:<br>
>a)对训练集进行第t次随机采样，共采集m次，得到包含m个样本的采样集Dt<br>
>b)用采样集Dt训练第t个弱学习器Gt(x)<br>
* 2）如果是分类算法预测，则T个弱学习器投出最多票数的类别或者类别之一为最终类别。
如果是回归算法，T个弱学习器得到的回归结果进行算术平均得到的值为最终的模型输出。<br>

## 3. 随机森林算法

理解了bagging算法，随机森林(Random Forest,以下简称RF)就好理解了。它是Bagging算法的进化版，也就是说，
它的思想仍然是bagging,但是进行了独有的改进。我们现在就来看看RF算法改进了什么。　　　

首先，RF使用了`CART决策树`作为弱学习器，这让我们想到了梯度提升树GBDT。
其次，在使用决策树的基础上，RF对决策树的建立做了改进，对于普通的决策树，
我们会在节点上所有的n个样本特征中选择一个最优的特征来做决策树的左右子树划分，
但是RF通过随机选择节点上的一部分样本特征，这个数字小于n，
假设为nsub，然后在这些随机选择的nsub个样本特征中，选择一个最优的特征来做决策树的左右子树划分。
这样进一步增强了模型的泛化能力。`即对样本和变量同时随机取样`　

如果nsub=n，则此时RF的CART决策树和普通的CART决策树没有区别。nsub越小，则模型越健壮，当然此时对于训练集的拟合程度会变差。
也就是说nsub越小，模型的方差会减小，但是偏倚会增大。在实际案例中，一般会通过交叉验证调参获取一个合适的nsub的值。

除了上面两点，RF和普通的bagging算法没有什么不同， 下面简单总结下RF的算法。

输入为样本集D={(x,y1),(x2,y2),...(xm,ym)}，弱分类器迭代次数T。<br>
输出为最终的强分类器f(x)<Br>

* 1）对于t=1,2...,T:
>a)对训练集进行第t次随机采样，共采集m次，得到包含m个样本的采样集Dt<Br>
b)用采样集Dt训练第t个决策树模型Gt(x)，在训练决策树模型的节点的时候， 在节点上所有的样本特征中选择一部分样本特征， 
在这些随机选择的部分样本特征中选择一个最优的特征来做决策树的左右子树划分
* 2）如果是分类算法预测，则T个弱学习器投出最多票数的类别或者类别之一为最终类别。
如果是回归算法，T个弱学习器得到的回归结果进行算术平均得到的值为最终的模型输出。

## 4. 随机森林的推广
由于RF在实际应用中的良好特性，基于RF，有很多变种算法，应用也很广泛，不光可以用于分类回归，还可以用于特征转换，异常点检测等。
下面对于这些RF家族的算法中有代表性的做一个总结。

### 4.1 extra trees

extra trees是RF的一个变种, 原理几乎和RF一模一样，仅有区别有：

>1） 对于每个决策树的训练集，RF采用的是随机采样bootstrap来选择采样集作为每个决策树的训练集，
而extra trees一般不采用随机采样，即每个决策树采用原始训练集。

>2） 在选定了划分特征后，RF的决策树会基于基尼系数，均方差之类的原则，选择一个最优的特征值划分点，
这和传统的决策树相同。但是extra trees比较的激进，他会随机的选择一个特征值来划分决策树。

从第二点可以看出，由于随机选择了特征值的划分点位，而不是最优点位，这样会导致生成的决策树的规模一般会大于RF所生成的决策树。
也就是说，模型的方差相对于RF进一步减少，但是偏倚相对于RF进一步增大。在某些时候，extra trees的泛化能力比RF更好。

### 4.2 Totally Random Trees Embedding
Totally Random Trees Embedding(以下简称 TRTE)是一种非监督学习的数据转化方法。它将低维的数据集映射到高维，
从而让映射到高维的数据更好的运用于分类回归模型。我们知道，在支持向量机中运用了核方法来将低维的数据集映射到高维，
此处TRTE提供了另外一种方法。

TRTE在数据转化的过程也使用了类似于RF的方法，建立T个决策树来拟合数据。当决策树建立完毕以后，
数据集里的每个数据在T个决策树中叶子节点的位置也定下来了。比如我们有3颗决策树，每个决策树有5个叶子节点，
某个数据特征x划分到第一个决策树的第2个叶子节点，第二个决策树的第3个叶子节点，第三个决策树的第5个叶子节点。
则x映射后的特征编码为(0,1,0,0,0,     0,0,1,0,0,     0,0,0,0,1), 有15维的高维特征。
这里特征维度之间加上空格是为了强调三颗决策树各自的子编码。

映射到高维特征后，可以继续使用监督学习的各种分类回归算法了。

### 4.3 Isolation Forest
Isolation Forest（以下简称IForest）是一种异常点检测的方法。它也使用了类似于RF的方法来检测异常点。

对于在T个决策树的样本集，IForest也会对训练集进行随机采样,但是采样个数不需要和RF一样，对于RF，
需要采样到采样集样本个数等于训练集个数。但是IForest不需要采样这么多，一般来说，采样个数要远远小于训练集个数？为什么呢？
因为我们的目的是异常点检测，只需要部分的样本我们一般就可以将异常点区别出来了。

对于每一个决策树的建立， IForest采用随机选择一个划分特征，对划分特征随机选择一个划分阈值。这点也和RF不同。

另外，IForest一般会选择一个比较小的最大决策树深度max_depth,原因同样本采集，用少量的异常点检测一般不需要这么大规模的决策树。

对于异常点的判断，则是将测试样本点x拟合到T颗决策树。计算在每颗决策树上该样本的叶子节点的深度ht(x)。，
从而可以计算出平均高度h(x)。此时我们用下面的公式计算样本点x的异常概率:<br>
s(x,m)=2?h(x)c(m)<br>
其中，m为样本个数。c(m)的表达式为：<br>
c(m)=2ln(m?1)+ξ?2m?1m,ξ为欧拉常数<br>
s(x,m)的取值范围是[0,1],取值越接近于1，则是异常点的概率也越大。<br>

## 5. 随机森林小结
RF的算法原理也终于讲完了，作为一个可以高度并行化的算法，RF在大数据时候大有可为。 这里也对常规的随机森林算法的优缺点做一个总结。

RF的主要优点有：
* 1） 训练可以高度并行化，对于大数据时代的大样本训练速度有优势。个人觉得这是的最主要的优点。
* 2） 由于可以随机选择决策树节点划分特征，这样在样本特征维度很高的时候，仍然能高效的训练模型。
* 3） 在训练后，可以给出各个特征对于输出的重要性
* 4） 由于采用了随机采样，训练出的模型的方差小，泛化能力强。
* 5） 相对于Boosting系列的Adaboost和GBDT， RF实现比较简单。
* 6） 对部分特征缺失不敏感。

RF的主要缺点有：
* 1）在某些噪音比较大的样本集上，RF模型容易陷入过拟合。
* 2）取值划分比较多的特征容易对RF的决策产生更大的影响，从而影响拟合的模型的效果。



# 四、梯度提升树(GBDT)原理小结
原文链接：https://www.cnblogs.com/pinard/p/6140514.html


# 五、scikit-learn Adaboost类库使用小结
原文链接：https://www.cnblogs.com/pinard/p/6136914.html


# 六、scikit-learn 梯度提升树(GBDT)调参小结
原文链接：https://www.cnblogs.com/pinard/p/6143927.html


# 七、scikit-learn随机森林调参小结
原文链接：https://www.cnblogs.com/pinard/p/6160412.html






