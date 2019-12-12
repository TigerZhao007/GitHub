
# ######################################################################################################################
# 理解'*','*args','**','**kwargs'
# https://blog.csdn.net/callinglove/article/details/45483097
# ######################################################################################################################
# 让我们通过以下5步来理解：
# 1. 通过一个函数调用来理解’*’的作用
# 2. 通过一个函数的定义来理解’*args’的含义
# 3. 通过一个函数的调用来理解’**’的作用
# 4. 通过一个函数的定义来解’**kwargs’的含义
# 5. 通过一个应用实例来说明’args’,’kwargs’应用场景以及为何要使用它

# ######################################################################################################################
# 通过一个函数调用来理解’*’的作用
# ######################################################################################################################

# ’*’的案例~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 定义一个含三个位置参数的函数”fun”.
def fun(a, b, c):
    print(a, b, c)

# 传三个位置参数调用此函数
fun(1, 2, 3)           # 1 2 3

# 现在我们定义一个含三个整数的数列，并使用’*’
lis = [1, 2, 3]
fun(*lis)              # 1 2 3

# ’*’的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 它拆开数列’l’的数值作为位置参数，并吧这些位置参数传给函数’fun’来调用。
# 因此拆数列、传位置参数意味着fun(*l)与fun(1,2,3)是等效的，因为l = [1,2,3]。试着数列中使用其他数值

# ’*’的错误案例~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 接下来我们试着在数列中放四个数值，调用函数会出现什么情况呢
lis = [3, 6, 9, 1]
fun(*lis)              # TypeError: fun() takes 3 positional arguments but 4 were given
# 在这次调用中我们并没有得到合适的结果，触发了TypeWrror异常。
# 很容易看到错误内容”fun() takes exactly 3 arguments (4 given)”.

lis = [7, 4]
fun(*lis)              # TypeError: fun() missing 1 required positional argument: 'c'

# 为什么会发生这种情况呢？
'''
数列’l’含有四个数值.因此，我们试图调用’fun(*l)’，’l’中数值拆开传给函数fun作为位置参数。
但是，’l’中有四个数值，调用’fun(*l)’相当于调用’fun(3,6,9,1)’,又因为函数’fun’定义中只用三个位置参数，
因此我们得到这个错误。同理，同样的步骤，数列’l’中有两个数值情况，注意error内容。
'''

# ‘*l’与位置参数混合使用
lis = [7, 4]
fun(23, *lis)          # 23 7 4

# ######################################################################################################################
# ‘*args’在函数定义中是做什么用的？
# ######################################################################################################################
# 它接收元组作为位置参数，而非是常见的参数列表。在这里，”args”是个元组。在我们解释中不要担心”常见的参数”这部分的理解，
# 这个会在接下来的例子中逐渐明了。在上个例子中，调用函数打印”args”时，他会打印元组中包含的所有数值。
# 我们重新定义函数，”*args”与”常规参数列表”混合使用

def fun(a, *args):
    print('a is ', a)
    print('args is ', args)

# 在这个函数定义中,参数”a”代表”常规参数列表”。传四个位置参数调用此函数:

fun(11, 12, 34, 43)             #  a is  11   # args is  (12, 34, 43)

# 很容易看到,’a’打印出为11，即第一个位置参数。’a’之后只一个参数’*args’.
# 因此，’args’接收除常规参数之外的位置参数作为元组。因此元组args作为元组接收12,34和43。
# 我们也可以传一个位置参数来调用此函数:
fun(91)                         # a is  91     # args is  ()

# 在这里，我们传的唯一一个参数分配给了常规参数’a’.因此,’args’接收到一个空元组。
# 既然我们获取了”args”,我们可以提取需要的数值来做我们想做的事情。重新定义”fun”:

def fun(a, *args):
    print(a)
    print("args can receive a tuple of any number of arguments, let's print all that.")
    for arg in args:
        print(arg)

fun(1, 5, 6, 7)

# args’既然是元组，我们就可以遍历它。
# 现在我们考虑使用所有能得到的参数的场景。我们需要使用两个函数，第一个函数带有任意个参数，
# 并通过另外一个函数计算除第一参数的其他参数之和。奇怪的用例，但我们只需回顾我们目前所做的。
# 我们的目的就是在一个函数中获取可变参数，并把这些参数餐给另一个函数。
# 第一步我们写一个函数计算和。在这个用例中，这个函数会在第一个函数中应用。

def calculate_sum(*args):
    return sum(args)

# 在这个函数中，我们使用内建函数’sum’,它使用元组或数列作为参数，返回元组所有元素的和。
# 从函数的定义可以看出’args’接收包含传给此函数位置参数的元组.因此,’args’是一个元组，简介的作为函数’sum’的参数。
# 接下来定义另外一个函数，该函数有任意个参数，并利用上一个函数来计算除第一个参数之外的其他参数的和。

def ignore_first_calculate_sum(a, *iargs):
    required_sum = calculate_sum(*iargs)
    print("sum is ", required_sum)

# 我们可以传任意个参数给这个函数。第一个参数被常规参数a接收，其他参数被iargs作为元组接收。
# 正如我们考虑的案例，计算除第一个参数之外的其他参数的和。因此，我们用a接收第一个参数,iargs是包含其他参数的元组。
# 我们用到函数calculate_sum，但calculate_sum需要多个位置参数作为元组传给args。
# 所以在函数ignore_first_calculate_sum需要拆元组iargs,然后将元素作为位置参数传给calculate_sum.注意,用*拆元组。
# 所以，我们这样调用required_sum=calculate_sum(*iargs).
# required_sum=calculate_sum(iargs)不能这么调用，因为传给calculate_sum之前我们需要unpack数值。
# 不使用*将不会unpack数值,也就不能执行想要的动作。调用函数如下:

ignore_first_calculate_sum(12, 1,4,5)        # sum is  10
ignore_first_calculate_sum()                 # TypeError: ignore_first_calculate_sum() takes at least 1 argument (0 given)


# ######################################################################################################################
# 通过一个函数的调用来理解’**’的作用
# ######################################################################################################################

# ’**’的案例~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 定义一个三个参数的函数,并用多种方式调用:
def fun(a, b, c):
    print((a, b, c))

fun(1, 5, 7)              # (1, 5, 7)
fun(a=1, b=5, c=7)        # (1, 5, 7)

# 使用”**”调用函数,这种方式我们需要一个字典.注意:在函数调用中使用”*”，
# 我们需要元组;在函数调用中使用”**”，我们需要一个字典

d = {'b': 5, 'c': 7}
fun(1, **d)                # (1, 5, 7)

# ’**’的作用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 它unpack字典，并将字典中的数据项作为键值参数传给函数。因此,”fun(1, **d)”的写法与”fun(1, b=5, c=7)”等效.

# ’**’的错误案例~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
d = {'a': 7, 'b': 3, 'c': 8, 'd': 90}
fun(**d)                # TypeError: fun() got an unexpected keyword argument 'd'
# 这次调用等同于’fun(a=7, b=3, c=8, d=90)’,但函数只需要三个参数，因此我们得到TypeError

d = {'a': 7, 'b': 3,'d': 90}
fun(**d)                # TypeError: fun() got an unexpected keyword argument 'd'
# fun(**d)等同于fun(a=7, b=3, d=90).传给函数”fun”想要的参数个数，但参数列表中并没有’d’,
# 调用中’d’键值参数传给函数导致TypeError.


# ######################################################################################################################
# 通过函数定义来理解’**kwargs’的含义
# ######################################################################################################################

def fun(a, **kwargs):
    print(a, kwargs)

# 此函数只用一个位置参数，因为常规参数列表中只有一个变量’a’.但是通过”**kwargs”,可以传多个键值参数。
fun(1, b=4, c=5)                 # 1 {'b': 4, 'c': 5}
fun(45, b=6, c=7, d=8)           # 45 {'b': 6, 'c': 7, 'd': 8}

# 在函数定义中”**kwargs”意味着什么？
# 用”**kwargs”定义函数,kwargs接收除常规参数列表职位的键值参数字典。在这里’kwargs’是个字典。

def fun(a, **kwargs):
    print("a is ", a)
    print("We expect kwargs 'b' and 'c' in this function")
    print("b is ", kwargs['b'])
    print("c is ", kwargs['c'])

fun(1, b=3, c=5)
# a is  1
# We expect kwargs 'b' and 'c' in this function
# b is  3
# c is  5

fun(1, b=3, d=5)
# a is  1
# We expect kwargs 'b' and 'c' in this function
# b is  3
# KeyError: 'c'

# 上面的调用,位置参数’a’和键值参数’b’都打印出来了。传入的其他键值参数是’d’，函数需要键值参数’c’，
# 并从字典’kwargs’获取。但没有传入键值’c’,引发KeyError.如果传入了键值’c’就不会引发这个错误

fun(1, b=3, d=5, c=9)
# a is  1
# We expect kwargs 'b' and 'c' in this function
# b is  3
# c is  9
# 由于’**kwargs’在函数参数列表中,我们可以传任意个键值参数。上面的调用传入了”d”，但函数并没用到。

fun(1, {'b': 2, 'c': 34})   # TypeError: fun() takes exactly 1 argument (2 given)
# 正如错误提示,函数’fun’只需要一个位置参数,却给了两个。尽管’kwargs’接收键值参数作为一个字典,
# 但你不能传一个字典作为位置参数给’kwargs’.你可以像下面那样调用:

fun(1, **{'b': 2, 'c': 34})
# a is  1
# We expect kwargs 'b' and 'c' in this function
# b is  2
# c is  34
# 在一个字典前使用”**”可以unpack字典,传字典中的数据项作为键值参数。

# ######################################################################################################################
# 通过一个应用实例来说明’args’,’kwargs’应用场景以及为何要使用它
# ######################################################################################################################
# 在任何时候继承类和重写方法的，我们应当用到’*args’和’**kwargs’将接收到的位置参数和键值参数给父类方法。
# 通过实例我们更好的理解:

class Model(object):
    def __init__(self, name):
        self.name = name
    def save(self, force_update=False, force_insert=False):
        if force_update and force_insert:
            raise ValueError("Cannot perform both operations")
            if force_update:
                print("Updated an existing record")
            if force_insert:
                print("Created a new record")

# 定义一个类，我们可以创建类的对象，类的对象有一个方法’save()’.假设类的对象可以通过save()方法保存到数据库中。
# 通过函数save()参数来决定是否在数据库中创建一条记录或者更新现存的记录。
# 构造一个新类，类有’Model’的行为，但我们只有检查一些条件后才会保存这个类的对象。
# 这个新类继承’Model’，重写’Model’的’save()’

class ChildModel(Model):
    def save(self, *args, **kwargs):
        if self.name=='abcd':
            super(ChildModel, self).save(*args, **kwargs)
        else:
            return None

# 实际上对应的保存动作发生在’Model’的’save’方法中。所以我们调用子类的的’save()’方法而非’Model’的方法.
# 子类ChildModel的’save()’接收任何父类save()需要的参数，并传给父类方法。
# 因此,子类’save()’方法参数列表中有”*args”和”**kwargs”,它们可以接收任意位置参数或键值参数,常规参数列表除外。

# 下面创建ChildModel实体并保存:
c = ChildModel('abcd')
c.save(force_insert=True)   # Created a new record
c.save(force_update=True)   # Updated an existing record

# 这里传兼职参数给对象的save()方法。调用的是子类的save(),It received a dictionary containing the keyword argument in
# kwargs. Then it used ** to unpack this dictionary as keyword arguments and then passed it to the superclass save().
# So, superclass save() got a keyword argument ‘force_insert’ and acted accordingly.
