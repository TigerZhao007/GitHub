
# ######################################################################################################################
# Python 获取当前文件路径方法
# ######################################################################################################################
import os
import sys

# 获取路径的函数说明~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
os.getcwd()
# 获取文件当前工作目录路径（绝对路径）

sys.path[0]
# 获取文件当前工作目录路径（绝对路径）, sys.argv[0]|获得模块所在的路径（由系统决定是否是全名）
# 若显示调用python指令，如python demo.py，会得到绝对路径;
# 若直接执行脚本，如./demo.py，会得到相对路径。

'__file__'
# 获得文件所在的路径（由系统决定是否是全名）
# 若显示执行Python，会得到绝对路径;
# 若按相对路径来直接执行脚本./pyws/path_demo.py，会得到相对路径。

os.path.abspath('__file__')
# 获得文件所在的路径（绝对路径）

os.path.realpath('__file__')
# 获得文件所在的路径（绝对路径）

os.path.split(os.path.realpath('__file__'))
# 将文件路径名称分成头和尾一对，生成二元元组。（文件目录，文件名）

# 获取路径的例子~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import sys

print("sys.path[0] = ", sys.path[0])
print("sys.argv[0] = ", sys.argv[0])
# print("__file__ = ", '__file__')  # 这里应该返回这个文件的完整路径，加上文件的名称？？？？
print("os.path.abspath(__file__) = ", os.path.abspath('__file__'))
print("os.path.realpath(__file__) = ", os.path.realpath('__file__'))
print("os.path.dirname(os.path.realpath(__file__)) = ", os.path.dirname(os.path.realpath('__file__')))  # 非完整路径
print("os.path.split(os.path.realpath(__file__)) = ", os.path.split(os.path.realpath('__file__')))  # 非完整路径
print("os.path.split(os.path.realpath(__file__))[0] = ", os.path.split(os.path.realpath('__file__'))[0])
print("os.getcwd() = ", os.getcwd())

