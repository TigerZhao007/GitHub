

# ######################################################################################################################
# 导入系统模块(import)
# ######################################################################################################################

# import 语句~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 导入模块
import math

print("求e的n次幂：", math.exp(1))

# from…import 语句~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 从模块中导入一个指定的部分到当前命名空间中, 导入模块中的特定函数
from math import exp

print("求e的n次幂：", exp(1))

# from…import* 语句~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 导入一个模块中的所有项目。然而这种声明不该被过多地使用
from math import *

# ######################################################################################################################
# 导入本地模块(import)
# ######################################################################################################################

# 1、自定义模块与所需要调用自定义模块的文件在同一文件夹下~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 这时的调用就较为简单了，直接导入即可
import setup

# 2、自定义模块与所需要调用自定义模块的文件不在同一文件夹下~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2.1、用1中的方法，把需要导入的文件一个一个手动拖到当前文件夹中
# 2.2、找到本地库的路径，然后将文件拷进去即可
# 2.3、我们在folder中新建一个__init__.py文件，此时的folder不再是一个普通的文件夹，而是一个包 package
# （1）想导入哪一个文件的话就只需在文件开头import folder.filename即可
# （2）记得要先将自定义库路径添加到Python的库路径中。
# 2.4、将自定义库的路径添加到Python的库路径中去，有如下两种方法：
# （1）动态的添加库路径。在程序运行过程中修改sys.path的值，添加自己的库路径
import sys
sys.path.append(r'your_path')

# （2）在Python安装目录下的\Lib\site-packages文件夹中建立一个.pth文件，内容为自己写的库路径。
# 示例如下：E:\\work\\Python\\http
