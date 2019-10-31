
# Python����淶�������淶
## ǰ��
Python ѧϰ֮�ã��������� Python �Ĵ���淶�����Լ����и���ʶ�������������ѧϰ����������ϰ��

## Ŀ¼
Python����淶

## һ����������
#### 1������
�����������, �ļ�һ��ʹ�� UTF-8 ����<br>
�����������, �ļ�ͷ���������#-*-coding:utf-8-*-��ʶ<br>
####2�������ʽ
##### 2.1������
ͳһʹ�� 4 ���ո��������
##### 2.2���п�
ÿ�д��뾡�������� 80 ���ַ�(����������¿�����΢���� 80 ��������ó��� 120)<br>

���ɣ�
* ���ڲ鿴 side-by-side �� diff ʱ���а���
* �����ڿ���̨�²鿴����
* ̫�������������ȱ��

##### 2.3������
��˵����Ȼ����ʹ��˫���ţ�������ʾʹ�õ����ţ���� ������ ����Ӧ��ʹ�� ������

* `��Ȼ����` ʹ��˫���� "..."<br>
���������Ϣ���ܶ�������� unicode��ʹ��u"�������"
* `������ʶ` ʹ�õ����� '...'<br>
���� dict ��� key
* `������ʽ` ʹ��ԭ����˫���� r"..."<br>
�ĵ��ַ��� (docstring) ʹ������˫���� """......"""

##### 2.4������
* ģ�鼶�������ඨ��֮������У�
* ���Ա����֮���һ�У�
```python
class A:
 
    def __init__(self):
        pass
 
    def hello(self):
        pass
 
def main():
    pass   
```
* ����ʹ�ö�����зָ�������صĺ���
* �����п���ʹ�ÿ��зָ����߼���صĴ���

##### 2.5������
* �ļ�ʹ�� UTF-8 ����
* �ļ�ͷ������#-*-conding:utf-8-*-��ʶ

#### 3��import ���
* import ���Ӧ�÷�����д
```python
# ��ȷ��д��
import os
import sys
 
# ���Ƽ���д��
import sys,os
 
# ��ȷ��д��
from subprocess import Popen, PIPE

```
* import���Ӧ��ʹ�� absolute import
```python
# ��ȷ��д��
from foo.bar import Bar
 
# ���Ƽ���д��
from ..bar import Bar
```
* import���Ӧ�÷����ļ�ͷ��������ģ��˵����docstring֮����ȫ�ֱ���֮ǰ��<br>
* import���Ӧ�ð���˳�����У�ÿ��֮����һ�����зָ�<br>
```
import os
import sys
 
import msgpack
import zmq
 
import foo
```
* ��������ģ����ඨ��ʱ������ʹ����Ե���
```python
from myclass import MyClass
```
* �������������ͻ�����ʹ�������ռ�
```
import bar
import foo.bar
 
bar.Bar()
foo.bar.Bar()
```
#### 4���ո�
* �ڶ�Ԫ��������߸���һ��[=,-,+=,==,>,in,is not, and]:
```python
# ��ȷ��д��
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
 
# ���Ƽ���д��
i=i+1
submitted +=1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
* �����Ĳ����б��У�֮��Ҫ�пո�
```python
# ��ȷ��д��
def complex(real, imag):
    pass
 
# ���Ƽ���д��
def complex(real,imag):
    pass
```
* �����Ĳ����б��У�Ĭ��ֵ�Ⱥ����߲�Ҫ��ӿո�
```python
# ��ȷ��д��
def complex(real, imag=0.0):
    pass
 
# ���Ƽ���д��
def complex(real, imag = 0.0):
    pass
```

* ������֮��������֮ǰ��Ҫ�Ӷ���Ŀո�
```python
#��ȷ��д��
spam(ham[1], {eggs: 2})
 
#���Ƽ���д��
spam( ham[1], { eggs : 2 } )
```
* �ֵ�����������֮ǰ��Ҫ����Ŀո�
```python
# ��ȷ��д��
dict['key'] = list[index]
 
# ���Ƽ���д��
dict ['key'] = list [index]
```
* ��ҪΪ���븳ֵ����ʹ�õĶ���ո�
```python
# ��ȷ��д��
x = 1
y = 2
long_variable = 3
 
# ���Ƽ���д��
x             = 1
y             = 2
long_variable = 3
```

#### 5������
Python ֧�������ڵĻ��С���ʱ�����������

* 1) �ڶ������������ŵ���ʼ��
```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```
* 2) �ڶ������� 4 ���ո���������ʼ���žͻ��е�����
```python
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```
ʹ�÷�б��\���У���Ԫ�����+ .��Ӧ��������ĩ�����ַ���Ҳ�����ô˷�����
```python
session.query(MyTable).\
        filter_by(id=1).\
        one()
 
print 'Hello, '\
      '%s %s!' %\
      ('Harry', 'Potter')
```
��ֹ������䣬��һ���а��������䣺
```python
# ��ȷ��д��
do_first()
do_second()
do_third()
 
# ���Ƽ���д��
do_first();do_second();do_third();
```
if/for/whileһ��Ҫ���У�
```python
# ��ȷ��д��
if foo == 'blah':
    do_blah_thing()
 
# ���Ƽ���д��
if foo == 'blah': do_blash_thing()
```

#### 6��docstring
docstring �Ĺ淶�����䱾�����㣺

* 1.���еĹ���ģ�顢�������ࡢ��������Ӧ��д docstring ��˽�з�����һ����Ҫ����Ӧ���� def ���ṩһ����ע����˵����
* 2.docstring �Ľ���"""Ӧ�ö�ռһ�У����Ǵ� docstring ֻ��һ�С�
```python
"""Return a foobar
Optional plotz says to frobnicate the bizbaz first.
"""
 
"""Oneline docstring"""
```
## ����ע��
#### 1��ע��
##### 1.1����ע��
��#���ź��һ�񣬶�����ÿ��зֿ���ͬ����Ҫ��#���ţ�
```python
# ��ע��
# ��ע��
#
# ��ע��
# ��ע��
```
#### 1.2����ע��
����ʹ�������ո�����ֿ���ע�ⲻҪʹ���������ע��
```python
# ��ȷ��д��
x = x + 1  # �߿�Ӵ�һ������
 
# ���Ƽ���д��(�������ע��)
x = x + 1 # x��1
```

##### 1.3������
�ڴ���Ĺؼ�����(��Ƚϸ��ӵĵط�), ��дע�͵�Ҫ����дע��

�Ƚ���Ҫ��ע�Ͷ�, ʹ�ö���ȺŸ���, ���Ը�����Ŀ, ͻ����Ҫ��
```python
app = create_app(name, options)
 
# =====================================
# �����ڴ˴���� get post��app·����Ϊ !!!
# =====================================
 
if __name__ == '__main__':
    app.run()
```
#### 2���ĵ�ע�ͣ�Docstring��
��Ϊ�ĵ���Docstringһ�������ģ��ͷ�������������ͷ����������python�п���ͨ�������__doc__�����ȡ�ĵ�.
�༭����IDEҲ���Ը���Docstring�����Զ���ʾ.

* �ĵ�ע���� """ ��ͷ�ͽ�β, ���в�����, ���ж���, ĩ�б��軻��, ������Google��docstring���ʾ��
```python
# -*- coding: utf-8 -*-
"""Example docstrings.
This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::
        $ python example_google.py
Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.
"""
```
* ��Ҫ���ĵ�ע�͸��ƺ�������ԭ��, ���Ǿ����������������, ���;�������ͷ���ֵ��
```python
#  ���Ƽ���д��(��Ҫд����ԭ�͵ȷϻ�)
def function(a, b):
    """function(a, b) -> list"""
    ... ...
 
#  ��ȷ��д��
def function(a, b):
    """���㲢����a��b��Χ�����ݵ�ƽ��ֵ"""
    ... ...
```
* �Ժ�������������ֵ�ȵ�˵������numpy��׼, ������ʾ
```python
def func(arg1, arg2):
    """������д������һ�仰�ܽ�(��: ����ƽ��ֵ).
    �����Ǿ�������.
    ����
    ----------
    arg1 : int
        arg1�ľ�������
    arg2 : int
        arg2�ľ�������
    ����ֵ
    -------
    int
        ����ֵ�ľ�������
    �ο�
    --------
    otherfunc : ��������������...
    ʾ��
    --------
    ʾ��ʹ��doctest��ʽ, ��`>>>`��Ĵ�����Ա��ĵ����Թ�����Ϊ���������Զ�����
    >>> a=[1,2,3]
    >>> print [x + 3 for x in a]
    [4, 5, 6]
    """
```
* �ĵ�ע�Ͳ�������Ӣ��, ����Ҫ��Ӣ�Ļ���
* �ĵ�ע�Ͳ���Խ��Խ��, ͨ��һ���仰�ܰ����˵�������
* ģ�顢�����ࡢ���з���, ��д�ĵ�ע�͵�, Ӧ�þ���д�ĵ�ע��

## ���������淶
#### 1��ģ��
* ģ�龡��ʹ��Сд����������ĸ����Сд��������Ҫ���»���(���Ƕ�����ʣ���������������)
```python
# ��ȷ��ģ����
import decoder

import html_parser# ���Ƽ���ģ����
import Decoder
```
#### 2������
* ����ʹ���շ�(CamelCase)�����������ĸ��д��˽�������һ���»��߿�ͷ
```python
class Farm():
    pass
 
class AnimalFarm(Farm):
    pass
 
class _PrivateFarm(Farm):
    pass
```
* ����ص���Ͷ�����������ͬһ��ģ����. ����Java, û��Ҫ����һ����һ��ģ��.
#### 3������
* ������һ��Сд�����ж�����ʣ����»��߸���
```python
def run():
    pass
 
def run_with_env():
    pass
```
* ˽�к����ں���ǰ��һ���»���_
```python
class Person():
 
    def _private_func():
        pass
```
#### 4��������
* ����������Сд, ���ж�����ʣ����»��߸���
```python
if __name__ == '__main__':
    count = 0
    school_name = ''
```
* ��������ȫ��д�����ж�����ʣ�ʹ���»��߸���
```python
MAX_CLIENT = 100
MAX_CONNECTION = 1000
CONNECTION_TIMEOUT = 600
```
#### 5������
* ����ʹ�����»��߷ָ��Ĵ�д����
```python
MAX_OVERFLOW = 100
 
Class FooBar:
 
    def foo_bar(self, print_):
        print(print_)
```









