# 如何加速R？

# 一. 优化R代码的方向
关于R的进阶教程比较著名的包括：《The art of R programming》、《Advanced R》、《The R inferno》三本书难度由浅到深，
分别从R语言常用的数据结构和操作，到R泛化函数，到最后如何从细节，习惯甚至思想上改进你的代码，都给出了非常漂亮的例子。<br>
总的来说，加速R代码可以从三个方面入手：
* R代码本身出发进行优化
* 利用并行运算
* 利用Rcpp和其他的运算库
对于这三个方向，我会持续的把自己遇见的问题记录在这里。这里强烈推荐用microbenchmark这个包对代码的运行时长进行测试。<br>

# 二. 加速方法说明
## 1. 从R代码出发
关于这一块，上面三本书，尤其是《The R inferno》已经介绍的非常详细了。我这里仅仅举几个常用的例子。<br>
* （1）尽量不使用中间变量，使用嵌套函数，或者直接返回表达式。这样避免了分配内存的时间。
* （2）向量化你的代码，避免单独操作。这个很好理解，批量操作总再取出来在放回去的快。当然，pply的函数组也是向量化操作的体现。
* （3）尽量使用已有的函数，因为这些函数已经包裹好了，甚至调用了专门用来计算的库。（当然这样需要你不停的多看多写）
* （4）尽量不使用循环，而使用pply组，replicate等函数。这些函数对你的操作进行包裹，从而提高运行速度。
## 2. 利用并行运算
我对R语言并行计算还只是浅薄的了解。关于并行运算，《Advanced R》里面只有微乎其微的讲解，
对于那些真正真正深入的人来说远远不够。这里可以用《Parallel R》，《Parallel Computing for Data Science》，这两本书进行学习实战。<br>
R常用的并行计算的库有很多，例如：snow，parallel，multicore等等。当然有的对windows不是特别的友善。这些并行大抵都遵循这样的思路：<br>
* 创建一个集群
* 把函数分割开来放入集群
* 以某种方式合并结果
* 关闭你的集群
因为我这里知之甚少，所以从《Parallel R》copy一个例子，来让大家体会。链接：<br>
https://link.zhihu.com/target=http%3A//detritus.fundacioace.com/pub/books/Oreilly.Parallel.R.Oct.2011.pdf
## 3. 利用Rcpp和其他的运算库
* Rcpp是提升R速度的强有力的工具。关于Rcpp的经典教材主要有：《Writing R Extensions》、《Seamless R and C++ Integration with Rcpp》
前面本算是个说明文档，后面这一本是在前面的基础上整理成的书，两个都可以看一下。<br>
先给一个计算fibonacci函数的例子。<br>
* 首先要写一个名字为fibonacci.cpp的函数，可以把如下的代码粘进去：然后我们在R语言里面同样的写一个fibonacci的函数，同时调用进行对比：
上面可以看出来Rcpp快了很多。<br>
* 有些时候，Rcpp不一定就R快。R本身的许多函数是用c包装好的，并且经过核心团队的优化，个人写出的函数很难超越。<br>
在针对不同的使用情况当中，你也可以借助一些其他的工具。关于线性代数的计算，就有很多方便的工具。
* 例如：RcppArmadillo是R团队开发的一个C++的线性代数计算库，具有非常快的运算速度。
当然，你也可以借助blas，mkl等等，这些都可以大大加速矩阵的计算。<br>

* 下面给一个矩阵乘法的例子，来看看：Rcpp，blas，R，RcppArmadillo哪个更快。这个例子的来源是Stack Overflow。<br>
* 虽然，blas在计算上已经非常强大，RcppArmadillo竟然表现的还要好。对于广大使用Rcpp的群众来说，RcppArmadillo无疑是一个强有力的矩阵计算工具了。<br>