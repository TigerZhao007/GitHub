

# 测试函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def func_test(n=100000000):
    result = 0
    for i in range(n):
        result += i
    return result

# ######################################################################################################################
# Python获取代码运行时间的几种方法
# ######################################################################################################################

# 方法1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# python 的标准库手册推荐在任何情况下尽量使用time.clock().
# 只计算了程序运行CPU的时间，返回值是浮点数
import time
start = time.clock()

# 中间写代码块
result = func_test(n=100000000)

end = time.clock()
print('Running time: %s Seconds' % (end-start))

# 方法2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 该方法包含了其他程序使用CPU的时间，返回值是浮点数
import time
start = time.time()

# 中间写代码块
result = func_test(n=100000000)

end = time.time()
print('Running time: %s Seconds' % (end-start))

# 方法3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 该方法包含了其他程序使用CPU的时间
import datetime
start = datetime.datetime.now()

# 中间写代码块
result = func_test(n=100000000)

end = datetime.datetime.now()
print('Running time: %s Seconds' % (end-start))

# 方法4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 在 Unix 系统中，建议使用 time.time()，在 Windows 系统中，建议使用 time.clock()
# 实现跨平台的精度性可以使用timeit.default_timer()
import timeit
start = timeit.default_timer()

# 中间写代码块
result = func_test(n=100000000)

end = timeit.default_timer()
print('Running time: %s Seconds' % (end-start))






