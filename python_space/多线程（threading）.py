# coding:utf-8

# #####################################################################################################################
# 单线程
'''
1.平常写的代码都是按顺序挨个执行的，就好比吃火锅和哼小曲这两个行为事件，定义成两个函数，执行的时候，是先吃火锅再哼小曲，这种就是单线程的行为。
2.生活中我们是可以一边吃火锅一边哼小曲的，那么代码里面如何实现这种同时进行的不同事件呢？这就是接下来要讲的python多线程
'''
# #####################################################################################################################
import time

def chi():
    print("%s 吃火锅开始：" % time.ctime())
    time.sleep(1)
    print("%s 吃火锅结束--" % time.ctime())

def heng():
    print("%s 哼着小曲开始:" % time.ctime())
    time.sleep(1)
    print("%s 哼着小曲结束--" % time.ctime())

if __name__ == "__main__":
    chi()
    heng()

# #####################################################################################################################
# 多线程
'''
1.Python通过两个标准库thread和threading提供对线程的支持。thread提供了低级别的、原始的线程以及一个简单的锁.Threading模块封装了一些常用的方法，初学者直接学这个模块就行了。
2.Python中使用线程有两种方式：函数或者用类来包装线程对象
3.threading.Thread里面几个参数介绍：
class Thread(_Verbose)
__init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None)
*group*：group参数必须为空，参数group是预留的，用于将来扩展；
参数args和kwargs分别表示调用target时的参数列表和关键字参数。
*target*: 参数target是一个可调用对象（也称为活动[activity]），在线程启动后执行
*name*: 参数name是线程的名字。默认值为“Thread-N“，N是一个数字。
*args*：传递给线程函数target的参数,他必须是个tuple类型.
*kwargs*：kwargs表示关键字参数。字典类型 {}.
'''
# #####################################################################################################################

# 1.先看个简单案例，这种是执行函数，函数不带参数的 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import threading
import time

def chi():
    print("%s 吃着火锅开始：" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：涮羊肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：涮牛肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：贡丸" % time.ctime())
    time.sleep(1)
    print("%s 吃火锅结束！" % time.ctime())

def ting():
    print("%s 哼着小曲1！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲2！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲3！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲4！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲5！" % time.ctime())
    time.sleep(2)

# 创建线程数组
threads = []
# 创建线程t1，并添加到线程数组
t1 = threading.Thread(target=chi)
threads.append(t1)
# 创建线程t2，并添加到线程数组
t2 = threading.Thread(target=ting)
threads.append(t2)
if __name__ == '__main__':    # 启动线程
    for t in threads:
        t.start()

# 2.带参数的用args传元组类型（参数最后多加一个逗号“,”要不然会报错）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# coding:utf-8
import threading
import time

def chi(threadName,name):
    print("%s 吃着%s开始：" % (time.ctime(),threadName))
    print("%s 吃着火锅：涮羊肉" % time.ctime())
    time.sleep(1)
    time.sleep(1)
    print("%s 吃着火锅：涮牛肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：贡丸" % time.ctime())
    time.sleep(1)
    print("%s 吃着%s结束--" % (time.ctime(),threadName))
    print("%s 运行结束！"%name)

def ting(threadName):
    print("%s 哼着%s1！" % (time.ctime(),threadName))
    time.sleep(2)
    print("%s 哼着小曲2！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲3！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲4！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲5！" % time.ctime())
    time.sleep(2)

# 创建线程数组

threads = []

# 创建线程t1，并添加到线程数组
# t1 = threading.Thread(target=chi, args=("火锅","吃火锅",))
# 传kwargs参数
t1 = threading.Thread(target=chi, kwargs={"threadName":"火锅","name":"吃火锅"})
threads.append(t1)

# 创建线程t2，并添加到线程数组
t2 = threading.Thread(target=ting,args=("小曲",))
threads.append(t2)

if __name__ == '__main__':    # 启动线程
    for t in threads:
        t.start()

# 3.或者用kwargs传字典{}类型 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 创建线程t1，并添加到线程数组
# t1 = threading.Thread(target=chi, args=("火锅","吃火锅",))
# 传kwargs参数
# t1 = threading.Thread(target=chi, kwargs={"threadName":"火锅","name":"吃火锅"})

# #####################################################################################################################
# 多线程threading之封装式
# https://cloud.tencent.com/developer/article/1087175
# #####################################################################################################################

# 一、执行函数 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''' 先写一个执行函数，用来实现做某件事情,不同的人吃火锅用一个参数people代替。'''
# coding=utf-8
import threading
import time

def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(),people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(),people))

# 二、 重写threading.Thread ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''使用Threading模块创建线程，直接从threading.Thread继承，然后重写__init__方法和run方法'''

# coding=utf-8
import threading
import time

class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, people, name):
        ''' 重写threading.Thread初始化内容 '''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        ''' 重写run方法 '''
        print("开始线程: " + self.threadName)
        chiHuoGuo(self.people)     # 执行任务
        print("qq交流群：226296743")
        print("结束线程: " + self.name)

# 三、 start和run区别 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
1.start()方法  开始线程活动。
对每一个线程对象来说它只能被调用一次，它安排对象在一个另外的单独线程中调用run()方法（而非当前所处线程）。
当该方法在同一个线程对象中被调用超过一次时，会引入RuntimeError(运行时错误)。
2.run()方法  代表了线程活动的方法。
你可以在子类中重写此方法。标准run()方法调用了传递给对象的构造函数的可调对象作为目标参数，
如果有这样的参数的话，顺序和关键字参数分别从args和kargs取得

备注：这里运行结果会有个问题，主线程已经退出了，子线程hread-1和Thread-2还在跑。这就是后面需要讲的守护线程了。。。
'''
# coding=utf-8
import threading
import time

def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(),people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(),people))

class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)
        chiHuoGuo(self.people)     # 执行任务
        print("结束线程: " + self.name)

# 创建新线程
thread1 = myThread("YOYO", "Thread-1")
thread2 = myThread("xiaowang", "Thread-2")

# 开启线程
thread1.start()
thread2.start()
time.sleep(1)
print("退出主线程")

# #####################################################################################################################
# python笔记9-多线程Threading之阻塞(join)和守护线程(setDaemon)
'''
今天小编YOYO请xiaoming和xiaowang吃火锅，吃完火锅的时候会有以下三种场景：
- 场景一：小编（主）先吃完了，xiaoming(客)和xiaowang(客)还没吃完，这种场景会导致结账的人先走了，剩下两个小伙伴傻眼了。
- 场景二：小编（主）先吃完了，xiaoming和xiaowang还没吃饱，一起结账走人。
- 场景三：小编（主）先等xiaoming和xiaowang吃饱了，小编最后结账一起走人。
'''
# #####################################################################################################################

# 一、 主线程与子线程~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
场景一：主线程已经结束了，子线程还在跑
1.我们把thread1.start()和thread2.start()称为两个子线程，写在外面的代码就是主线程了。
'''
# coding=utf-8
import threading
import time

def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(),people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(),people))

class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)
        chiHuoGuo(self.people)     # 执行任务
        print("结束线程: " + self.name)

print("yoyo请小伙伴开始吃火锅：！！！")

# 创建新线程
thread1 = myThread("xiaoming", "Thread-1")
thread2 = myThread("xiaowang", "Thread-2")

# 开启线程
thread1.start()
thread2.start()
time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")

# 二、 守护线程setDaemon() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
场景二：主线程结束了，子线程必须也跟着结束
1.主线程中，创建了子线程thread1和thread2，并且在主线程中调用了thread.setDaemon(),这个的意思是，把主线程设置为守护线程，
这时候，要是主线程执行结束了，就不管子线程是否完成,一并和主线程退出.
（敲黑板：必须在start()方法调用之前设置，如果不设置为守护线程，程序会被无限挂起。）
2.线程有一个布尔属性叫做daemon。表示线程是否是守护线程，默认取否。当程序中的线程全部是守护线程时，程序才会退出。
只要还存在一个非守护线程，程序就不会退出。主线程是非守护线程。
3.setDaemon(True)此方法里面参数设置为True才会生效
'''
# coding=utf-8
import threading
import time

def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(),people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(),people))

class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)
        chiHuoGuo(self.people)     # 执行任务
        print("结束线程: " + self.name)

print("yoyo请小伙伴开始吃火锅：！！！")

# 创建新线程
thread1 = myThread("xiaoming", "Thread-1")
thread2 = myThread("xiaowang", "Thread-2")

# 守护线程setDaemon(True)
thread1.setDaemon(True)       # 必须在start之前
thread2.setDaemon(True)

# 开启线程
thread1.start()
thread2.start()
time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")

# 三、 阻塞主线程join(timeout)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
1.如果想让主线程等待子线程结束后再运行的话，就需要用到join(),此方法是在start之后（与setDaemon相反）
2.join(timeout)此方法有个timeout参数，是线程超时时间设置。
'''
# coding=utf-8
import threading
import time

def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(),people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(),people))

class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)
        chiHuoGuo(self.people)     # 执行任务
        print("结束线程: " + self.name)

print("yoyo请小伙伴开始吃火锅：！！！")
# 创建新线程
thread1 = myThread("xiaoming", "Thread-1")
thread2 = myThread("xiaowang", "Thread-2")
# 开启线程
thread1.start()
thread2.start()
# 阻塞主线程，等子线程结束
thread1.join()
thread2.join()
time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")

# #####################################################################################################################
# python笔记10-多线程之线程同步（锁lock）
'''
关于吃火锅的场景，小伙伴并不陌生，吃火锅的时候a同学往锅里下鱼丸，b同学同时去吃掉鱼丸，有可能会导致吃到生的鱼丸。
为了避免这种情况，在下鱼丸的过程中，先锁定操作，让吃火锅的小伙伴停一会，等鱼丸熟了再开吃，那么python如何模拟这种场景呢？
'''
# #####################################################################################################################

# 一、未锁定~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
1.如果多个线程同时操作某个数据，会出现不可预料的结果。比如以下场景：当小伙伴a在往火锅里面添加鱼丸的时候，
小伙伴b在同时吃掉鱼丸，这很有可能导致刚下锅的鱼丸被夹出来了（没有熟），或者还没下锅，就去夹鱼丸（夹不到）。
'''
# coding=utf-8
import threading
import time

def chiHuoGuo(people, do):
    print("%s 吃火锅的小伙伴：%s" % (time.ctime(),people))
    time.sleep(1)
    for i in range(3):
        time.sleep(1)
        print("%s %s正在 %s 鱼丸"% (time.ctime(), people, do))
    print("%s 吃火锅的小伙伴：%s" % (time.ctime(),people))

class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, people, name, do):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people
        self.do = do

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)
        chiHuoGuo(self.people, self.do)     # 执行任务
        print("结束线程: " + self.name)
print("yoyo请小伙伴开始吃火锅：！！！")

# 设置线程组
threads = []

# 创建新线程
thread1 = myThread("xiaoming", "Thread-1", "添加")
thread2 = myThread("xiaowang", "Thread-2", "吃掉")

# 添加到线程组
threads.append(thread1)
threads.append(thread2)

# 开启线程
for thread in threads:
    thread.start()

# 阻塞主线程，等子线程结束
for thread in threads:
    thread.join()
time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")

# 二、 线程同步（锁lock)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
1.为了避免以上这种情况发生，就引入锁的概念，锁有两种状态：锁定和未锁定
2.每当一个线程a要访问共享数据时，必须先获得锁定；如果已经有别的线程b获得锁定了，那么就让线程a暂停，也就是同步阻塞；
  等到线程b访问完毕，释放锁以后，再让线程a继续。
3.用threading.Lock()这个类里面的两个方法
- acquire() 锁住
- release() 释放锁
'''
# coding=utf-8
import threading
import time

def chiHuoGuo(people, do):
    print("%s 吃火锅的小伙伴：%s" % (time.ctime(),people))
    time.sleep(1)
    for i in range(3):
        time.sleep(1)
        print("%s %s正在 %s 鱼丸"% (time.ctime(), people, do))
    print("%s 吃火锅的小伙伴：%s" % (time.ctime(),people))

class myThread (threading.Thread):   # 继承父类threading.Thread
    lock = threading.Lock()  # 线程锁
    def __init__(self, people, name, do):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people
        self.do = do

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)
        # 执行任务之前锁定线程
        self.lock.acquire()
        chiHuoGuo(self.people, self.do)     # 执行任务
        # 执行完之后，释放锁
        self.lock.release()
        print("结束线程: " + self.name)
print("yoyo请小伙伴开始吃火锅：！！！")

# 设置线程组
threads = []

# 创建新线程
thread1 = myThread("xiaoming", "Thread-1", "添加")
thread2 = myThread("xiaowang", "Thread-2", "吃掉")

# 添加到线程组
threads.append(thread1)
threads.append(thread2)
# threads.append(thread1)

# 开启线程
for thread in threads:
    thread.start()

# 阻塞主线程，等子线程结束
for thread in threads:
    thread.join()
time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")

# #####################################################################################################################
# python笔记11-多线程之Condition（条件变量）
'''
当小伙伴a在往火锅里面添加鱼丸，这个就是生产者行为；另外一个小伙伴b在吃掉鱼丸就是消费者行为。
当火锅里面鱼丸达到一定数量加满后b才能吃，这就是一种条件判断了。
这就是本篇要讲的Condition（条件变量）
'''
# #####################################################################################################################

# 一、Condition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，
否则它将自己生成一个RLock实例。
可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于状态图中的等待阻塞状态，
直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。
Condition():
- acquire(): 线程锁
- release(): 释放锁
- wait(timeout): 线程挂起，直到收到一个notify通知或者超时（可选的，浮点数，单位是秒s）才会被唤醒继续运行。
wait()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。 
- notify(n=1): 通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正等待该condition的线程,
最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。notify()不会主动释放Lock。
- notifyAll(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程.
'''
# 二、 生产者与消费者~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# coding=utf-8
import threading
import time

con = threading.Condition()
num = 0

# 生产者
class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # 锁定线程
        global num
        con.acquire()
        while num < 5:
            print ("开始添加！！！")
            num += 1
            print ("火锅里面鱼丸个数：%s" % (str(num)))
            time.sleep(1)
        if num >= 5:
            print ("火锅里面里面鱼丸数量已经到达5个，无法添加了！")
            # 唤醒等待的线程
            con.notify()  # 唤醒小伙伴开吃啦
        # 释放锁
        con.release()

# 消费者
class Consumers(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        con.acquire()
        global num
        while num > 0:
            print ("开始吃啦！！！")
            num -= 1
            print ("火锅里面剩余鱼丸数量：%s" % (str(num)))
            time.sleep(2)
        if num <= 0:
            print ("锅底没货了，赶紧加鱼丸吧！")
            con.wait()
        con.release()

a = Producer()
b = Consumers()
a.start()
b.start()



