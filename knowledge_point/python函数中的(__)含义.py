
# ######################################################################################################################
# python __xx__函数介绍
# ######################################################################################################################

# '__name__'模块的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
Python使用缩进对齐组织代码的执行，所有没有缩进的代码，都会在载入时自动执行。每个文件（模块）都可以任意写一些没有缩进的代码，
并在载入时自动执行。为了区分 主执行代码和被调用文件，Python引入了变量：__name__。
1）当文件是被调用时，__name__的值为模块名；
2）当文件被执行时，__name__的值为 ‘__main__’。

Python中的模块（.py文件）在创建之初会自动加载一些内建变量，__name__就是其中之一。Python模块中通常会定义很多变量和函数，
这些变量和函数相当于模块中的一个功能，模块被导入到别的文件中，可以调用这些变量和函数。
那么这时 __name__ 的作用就彰显了，它可以标识模块的名字，可以显示一个模块的某功能是被自己执行还是被别的文件调用执行，
假设模块A、B，模块A自己定义了功能C,模块B调用模块A，现在功能C被执行了：
如果C被A自己执行，也就是说模块执行了自己定义的功能，那么 __name__=='__main__'
如果C被B调用执行，也就是说当前模块调用执行了别的模块的功能，那么__name__=='A'（被调用模块的名字）

上面的 __main__ 在python中作可以为函数的入口，而实际工程常用 if __name__=='__main__'来表示整个工程开始运行的入口。
此外你如果不想让功能的某部分被别的模块调用执行，比如我自定的模块Student里的‘我的密码是xxx’,只有自己执行才可以打印密码。
所有你可以把部分写在if语句里，只有__name__=='__main__'的时候才能执行。
这个可以这么理解，在if语句之外代码是最外层的，有点“全局变量”的意思，放入if里面就成了私有的了。
'''

# '__file__ '模块的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# __file__ ：当前文件路径
print('__file__')     # print(__file__)报错,__file__


# '__doc__  '模块的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# __doc__ ： 当前文件描述
print(__doc__)        # Automatically created module for IPython interactive environment

# '__main__'模块的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('__main__')     # print(__main__)报错,__main__

# '__int__'模块的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 使用Python写过面向对象的代码的同学，可能对__init__方法已经非常熟悉了，__init__方法通常用在初始化一个类实例的时候。
# 例如：
class Person(object):
    """Silly Person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)

if __name__ == '__main__':
    piglei = Person('piglei', 24)
    print(piglei)

# 这样便是__init__最普通的用法了。但__init__其实不是实例化一个类的时候第一个被调用的方法。
# 当使用Persion(name, age)这样的表达式来实例化一个类时，最先被调用的方法其实是__new__方法。

# '__new__'模块的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# __new__方法接受的参数虽然也是和__init__一样，但__init__是在类实例创建之后调用，而__new__方法正是创建这个类实例的方法。

class Person(object):
    """Silly Person"""
    def __new__(cls, name, age):
        print('__new__ called.')
        return super(Person, cls).__new__(cls, name, age)

    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)

if __name__ == '__main__':
    piglei = Person('piglei', 24)
    print(piglei)

# 执行结果：
# piglei @ macbook - pro: blog$ python new_and_init.py
# __new__called.
# __init__called.
# < Person: piglei(24) >

# 通过运行这段代码，我们可以看到，__new__方法的调用是发生在__init__之前的。
# 其实当你实例化一个类的时候，具体的执行逻辑是这样的：

'''
# 1、p = Person(name, age)
# 2、首先执行使用name和age参数来执行Person类的__new__方法，这个__new__方法会返回Person类的一个实例（通常情况下是使用
# super(Persion, cls).__new__(cls, … …) 这样的方式）
# 3、然后利用这个实例来调用类的__init__方法，上一步里面__new__产生的实例也就是__init__里面的的self。
# 所以，__init__和__new__最主要的区别在于：
# （1）__init__通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性，做一些额外的操作，
# 发生在类实例被创建完以后。它是实例级别的方法。
# （2）__new__通常用于控制生成一个新实例的过程。它是类级别的方法。
# 但是说了这么多，__new__最通常的用法是什么呢，我们什么时候需要__new__？

依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 
提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass。
首先我们来看一下第一个功能，具体我们可以用int来作为一个例子：
假如我们需要一个永远都是正数的整数类型，通过集成int，我们可能会写出这样的代码。
'''
class PositiveInteger(int):
    def __init__(self, value):
        super(PositiveInteger, self).__init__(self, abs(value))
i = PositiveInteger(-3)
print(i)

'''通过重载__new__方法，我们实现了需要的功能。另外一个作用，关于自定义metaclass。其实我最早接触__new__的时候，
就是因为需要自定义 metaclass，但鉴于篇幅原因，我们下次再来讲python中的metaclass和__new__的关系。'''

# 用__new__来实现单例
'''事实上，当我们理解了__new__方法后，我们还可以利用它来做一些其他有趣的事情，比如实现设计模式中的单例模式(singleton) 。
因为类每一次实例化后产生的过程都是通过__new__来控制的，所以通过重载__new__方法，我们可以很简单的实现单例模式。'''
class Singleton(object):
    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

obj1 = Singleton()
obj2 = Singleton()
obj1.attr1 = 'value1'
print(obj1.attr1, obj2.attr1)
print(obj1 is obj2)

'''知识点：
（1）继承自object的新式类才有__new__
（2）__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
（3）__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，
可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
（4）__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，
__init__不需要返回值
（5）若__new__没有正确返回当前类cls的实例，那__init__是不会被调用的，即使是父类的实例也不行
'''
class A(object):
    pass
class B(A):
    def __init__(self):
        print("init")

    def __new__(cls, *args, **kwargs):
        print("new %s" % cls)
        return object.__new__(A, *args, **kwargs)

b = B()
print(type(b))

# '__all__'模块的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ######################################################################################################################
# if __name__ == '__main__'模块的作用
# ######################################################################################################################

# if __name__ == '__main__'模块的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if __name__ == '__main__':
#     statements

# 这段代码的主要作用主要是让该python文件既可以独立运行，也可以当做模块导入到其他文件。
# 当导入到其他的脚本文件的时候，此时__name__的名字其实是导入模块的名字，不是’__main__’, main代码里面的就不执行了。

# 案例1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''只要你创建了一个模块（一个.py文件），这个模块就有一个内置属性name生成，该模块的 name 的值取决于如何应用这个模块。
即：如果你直接运行该模块，那么__name__ == "__main__"，如果你 import 一个模块，那么模块name 的值通常为模块文件名。
'''
# 1、创建一个test1.py：
'''
def func():
    print('hello, world!')

if __name__ == "__main__":
    func()
'''

# 模块中，首先定义了函数func()，用来打印出hello, world!，然后判断__name__ 是否等于 __main__，如果等于，有打印，
# 反之则反，现在运行该模块，结果为：hello, world!
# 说明__name__ 等于 __main__。

# 2、再创建一个test2.py：
'''
import test1
print('bye, world!')
'''
# 模块中，首先import test1，然后打印bye, world!做测试用，运行该模块，结果为：bye, world!
# 运行结果仅有bye, world!，说明__name__ 不等于 __main__。
# 通过上面test1.py和test2.py两个模块，我们现在可以得出一个非常实用的结论： 如果模块是被直接运行的，则代码块被运行，
# 如果模块被import，则代码块不被运行。

# ######################################################################################################################
# python '__init__.py'&'__main__.py'模块的作用
# ######################################################################################################################

# '__init__.py'&'__main__.py'模块的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 如果你希望 python 将一个文件夹作为 Package 对待，那么这个文件夹中必须包含一个名为 __init__.py 的文件，即使它是空的。
# 如果你需要 python 将一个文件夹作为 Package 执行，那么这个文件夹中必须包含一个名为 __main__.py 的文件。

# 案例1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 在__init__.py写入如下内容：
import sys
print('__init__')
print('__init__.__name__', __name__)
print('__init__.__package__', __package__)

# 在__main__.py写入如下内容：
import sys
print('__main__')
print('__main__.__name__', __name__)
print('__main__.__package__', __package__)
print('sys.path', sys.path)

# 执行 python pkg 和 python -m pkg，对比一下它们的输出结果,可以看出：
'''
(a) 当作文件夹执行的时候，__init__.py 不会被执行。在 __main__.py 来说，打印的变量 __package__ 是一个空字符串。
当作模块执行的时候，会先执行 __init__.py ，再执行 __main__.py 。
对于 __main__.py 来说，变量 __package__ 是 Package 的名字（pkg）。
另外， __init__.py 和 __main__.py 中的 __name__变量的值也是不同的。

(b) 对于一个 Package 来说，既然 __init__.py 必须存在，并且当作为模块执行的时候，它会先执行，
我们就应该把入口函数 main() 定义在 __init__.py 中。
当我们使用模块方式 -m 执行的时候， __init__.py 定义了 main() 函数，
然后在 __main__.py 中调用它，就能实现我们统一入口的目的。
'''

# 案例2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 对 __init__.py 做如下修改：
import sys
print('__init__')
print('__init__.__name__', __name__)
print('__init__.__package__', __package__)
print('sys.path', sys.path)
def main():
    print('__init__.main()')

# 对 __main__.py 做如下修改：
import sys
print('__main__')
print('__main__.__name__', __name__)
print('__main__.__package__', __package__)
print('sys.path', sys.path)
import pkg
pkg.main()

'''
python pkg ，调用失败原因在于sys.path 的第一个搜索路径pkg，但作为文件夹执行时package确是一个是空字符串（找不到）。
对于 python pkg 的调用方式来说，由于 __init__.py 没有被载入，python 解释器并不知道自己正在一个 Package 下面工作。
默认的，python 解释器将 __main__.py 的当前路径 pkg 加入 sys.path 中，然后在这个路径下面寻找 pkg 这个模块。
显然， pkg 文件夹下面并没有 pkg 这个模块，因此出错。
对于 python -m pkg 的调用方式来说，由于 __init__.py 被事先载入，此时 python 解释器已经知道了这是一个 package ，
因此当前路径（空字符串）被包含在 sys.path 中。然后再调用 __main__.py ，这时 import pkg 这个包就没有问题了。
而要理解这点，就要明白 __init__.py 是 python 解释器将当前文件夹作为 Package 处理的必要条件。
如果没有读取到 __init__.py ，python 就不会认为当前的文件夹是一个 Package，而只是把它当作普通文件夹来处理。
既然找到了问题原因，那么只需要把当前路径加入到 sys.path 中，就能解决这个问题。
'''

# 修改后的 __main__.py 如下：
import sys
print('__main__')
print('__main__.__name__', __name__)
print('__main__.__package__', __package__)
if not __package__:
    import os
    path = os.path.join(os.path.dirname(__file__), os.pardir)
    sys.path.insert(0, path)
    del os
print('sys.path', sys.path)
import pkg
pkg.main()

'''
看到这里，有人可能会提出两个问题：
1. 为什么不直接在 sys.path 前面加上一个空字符串来解决问题呢？ 
答：因为，如果不是在当前路径下调用，空字符串就没效果了，比如执行 python /path/to/pkg。

2. 为什么不用 if __package__ == '' 来判断 __package__ 的值呢？
答：这并不是偷懒。因为可能会出现这种调用（不推荐）： python pkg/__main__.py 。
而这种情况下， __package__ 的值就是 None 而不是 '' 了。
'''

# ######################################################################################################################
# python _、__、__xx__之间的差别
# ######################################################################################################################
'''
默认情况下，Python中的成员函数和成员变量都是公开的(public),
在python中没有类public,private等关键词来修饰成员函数和成员变量。
其实，Python并没有真正的私有化支持，但可用下划线得到伪私有。尽量避免定义以下划线开头的变量！
（1）_xxx ："单下划线 " 开始的成员变量叫做保护变量，意思是只有类实例和子类实例能访问到这些变量，
需通过类提供的接口进行访问；不能用'from module import *'导入
（2）__xxx ：类中的私有变量/方法名 （Python的函数也是对象，所以成员方法称为成员变量也行得通。）,
" 双下划线 " 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
（3）__xxx__ ：系统定义名字，前后均有一个“双下划线” 代表python里特殊方法专用的标识，
如 __init__（）代表类的构造函数。
'''
#-*- coding:utf-8 -*-

class A(object):
    def __init__(self):  # 系统定义方法
        self.string='A string'
        self._string='A _string'
        self.__string='A __string'  # 私有变量

    def fun(self):
        return self.string + ' fun-A'

    def _fun(self):
        return self._string+'  _fun-A'

    def __fun(self):   # 私有方法
        return self.__string+' __fun-A'

    def for__fun(self):   # 内部调用私有方法
        return self.__fun()

class B(A):
    def __init__(self):  # 系统定义方法
        self.string = 'B string'

a = A()
print(a.string)                                 # A string
print(a._string)                                # A _string
# print a.__string 不可访问

print(a.fun())                                  # A string fun-A
print(a._fun())                                 # A _string  _fun-A
# print(a.__fun() 不可访问
print(a.for__fun())                             # A __string __fun-A

b = B()
print(b.fun())                                  # B string fun-A
print(b.fun().__len__())  # 系统定义函数        # 14


