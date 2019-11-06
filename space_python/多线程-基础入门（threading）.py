# coding:utf-8

# #####################################################################################################################
# 单线程
'''
1.平常写的代码都是按顺序挨个执行的，就好比吃火锅和哼小曲这两个行为事件，定义成两个函数，执行的时候，是先吃火锅再哼小曲，
这种就是单线程的行为。
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
1.Python通过两个标准库thread和threading提供对线程的支持。thread提供了低级别的、原始的线程以及一个简单的锁.
Threading模块封装了一些常用的方法，初学者直接学这个模块就行了。
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

# #####################################################################################################################
# python笔记12-python多线程之事件(Event)
'''
小伙伴a,b,c围着吃火锅，当菜上齐了，请客的主人说：开吃！，于是小伙伴一起动筷子，这种场景如何实现
'''
# #####################################################################################################################

# 一、 Event（事件）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
Event（事件）：事件处理的机制：全局定义了一个内置标志Flag，如果Flag值为 False，那么当程序执行 event.wait方法时就会阻塞，
如果Flag值为True，那么event.wait 方法时便不再阻塞。
Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。
Event()
- set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。 
- clear(): 将标志设为False。 
- wait(timeout): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。
- isSet(): 获取内置标志状态，返回True或False。 
'''
# 二、 Event案例1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
场景：小伙伴a和b准备就绪，当收到通知event.set()的时候，会执行a和b线程
'''
# coding:utf-8
import threading
import time

event = threading.Event()

def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print ('%s 已经启动' % threading.currentThread().getName())
    print ('小伙伴 %s 已经进入就餐状态！'%name)
    time.sleep(1)
    event.wait()
    # 收到事件后进入运行状态
    print ('%s 收到通知了.' % threading.currentThread().getName())
    print ('小伙伴 %s 开始吃咯！'%name)

# 设置线程组
threads = []

# 创建新线程
thread1 = threading.Thread(target=chihuoguo, args=("a", ))
thread2 = threading.Thread(target=chihuoguo, args=("b", ))

# 添加到线程组
threads.append(thread1)
threads.append(thread2)

# 开启线程
for thread in threads:
    thread.start()
time.sleep(0.1)

# 发送事件通知
print ('主线程通知小伙伴开吃咯！')
event.set()

# 二、 Event案例2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
场景：当小伙伴a,b,c集结完毕后，请客的人发话：开吃咯！
'''
# coding:utf-8
import threading
import time

event = threading.Event()

def chiHuoGuo(name):
    # 等待事件，进入等待阻塞状态
    print ('%s 已经启动' % threading.currentThread().getName())
    print ('小伙伴 %s 已经进入就餐状态！'%name)
    time.sleep(1)
    event.wait()

    # 收到事件后进入运行状态
    print ('%s 收到通知了.' % threading.currentThread().getName())
    print ('%s 小伙伴 %s 开始吃咯！'%(time.ctime(), name))

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
        print("qq交流群：226296743")
        print("结束线程: " + self.name)

# 设置线程组
threads = []

# 创建新线程
thread1 = threading.Thread(target=chiHuoGuo, args=("a", ))
thread2 = threading.Thread(target=chiHuoGuo, args=("b", ))
thread3 = threading.Thread(target=chiHuoGuo, args=("c", ))

# 添加到线程组
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# 开启线程
for thread in threads:
    thread.start()
time.sleep(0.1)

# 发送事件通知
print ('YOYO:集合完毕，人员到齐了，开吃咯！')
event.set()

# #####################################################################################################################
# python笔记13-多线程实践篇（tomorrow）
'''
前面几篇连续讲解了多线程的一些概念，都是一些理论的东西，有了一些理论基础了，接下来就让我们把所学的知识用到实践中吧！
https://cloud.tencent.com/developer/article/1087164
算术入门（兔子实例）
例题1.7
'''
# #####################################################################################################################

# 一、 单线程~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
1.以下案例是单线程时候跑的情况，在下载图片的时候很耗时。
'''
# coding:utf-8
from bs4 import BeautifulSoup
import requests
import os
import time

# 当前脚本所在的目录
cur_path = os.path.dirname(os.path.realpath('__file__'))

def get_img_urls():
    r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
    fengjing = r.content
    soup = BeautifulSoup(fengjing, "html.parser")
    # 找出所有的标签
    images = soup.find_all(class_="lazy")
    return images

def save_img(imgUrl):
    try:
        jpg_rl = imgUrl["data-original"]
        title = imgUrl["title"]
        # 判断是否有jpg文件夹，不存在创建一个
        save_file = os.path.join(cur_path, "jpg")
        if not os.path.exists(save_file): os.makedirs(save_file)
        with open(os.path.join(save_file, title+'.jpg'), "wb") as f:
            f.write(requests.get(jpg_rl).content)
    except:
        pass

if __name__ == "__main__":
    t1 = time.time()
    image_ulrs = get_img_urls()
    for i in image_ulrs:
        save_img(i)
    t2 = time.time()
    print("总耗时：%.2f 秒"%(t2-t1))

# 二、 使用多线程tomorrow~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
1. 一行代码搞定多线程，在函数上加个@threads(5)，括号里面代码线程的数量，数字越大，运行的速度越快；
但是数字也不是越大越好，一般在5-10之间。
2. tomorrow 模块，该模块属于第三方的一个模块，使用起来非常的方便，只需要用其中的 threads 方法作为装饰器去修饰一个普通的函数，
既可以达到并发的效果，本篇将用实例来展示 tomorrow 的强大之处。后面将对 tomorrow 的实现原理做进一步的分析。
'''
# coding:utf-8
from bs4 import BeautifulSoup
import requests
import os
import time
from tomorrow import threads

# 当前脚本所在的目录
cur_path = os.path.dirname(os.path.realpath('__file__'))

def get_img_urls():
    r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
    fengjing = r.content
    soup = BeautifulSoup(fengjing, "html.parser")
    # 找出所有的标签
    images = soup.find_all(class_="lazy")
    return images

# 一行代码搞定多线程，在函数上加个@threads(5)，括号里面代码线程的数量，数字越大，运行的速度越快
@threads(5)
def save_img(imgUrl):
    try:
        jpg_rl = imgUrl["data-original"]
        title = imgUrl["title"]
        # print(title)
        # print(jpg_rl)
        # print("")
        # 判断是否有jpg文件夹，不存在创建一个
        save_file = os.path.join(cur_path, "jpg")
        if not os.path.exists(save_file): os.makedirs(save_file)
        with open(os.path.join(save_file, title+'.jpg'), "wb") as f:
            f.write(requests.get(jpg_rl).content)
    except:
        pass

if __name__ == "__main__":
    t1 = time.time()
    image_ulrs = get_img_urls()
    for i in image_ulrs:
        save_img(i)
    t2 = time.time()
    print("总耗时：%.2f 秒"%(t2-t1))

# #####################################################################################################################
# python－多线程和线程池
'''
传统多线程方案会使用“即时创建， 即时销毁”的策略。
from multiprocessing.dummy import Pool   # 线程池  （这是进程池from multiprocessing import Pool）
使用线程池：
由于线程预先被创建并放入线程池中，同时处理完当前任务之后并不销毁而是被安排处理下一个任务，因此能够避免多次创建线程，
从而节省线程创建和销毁的开销，能带来更好的性能和系统稳定性。
'''
# #####################################################################################################################

# 导入线程池模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time
from multiprocessing.dummy import Pool as ThreadPool  #给线程池取一个别名ThreadPool

# 定义测试运行函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def testRun(n):
  time.sleep(2)
  print(n)

# 采用线程池实现多线程~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
  li = [1, 2, 3, 4, 5]
  pool = ThreadPool(10)  # 创建10个容量的线程池并发执行
  pool.map(testRun, li)  # pool.map同map用法
  pool.close()
  pool.join()