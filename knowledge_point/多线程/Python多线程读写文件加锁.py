

# Python的多线程在io方面比单线程还是有优势，但是在多线程开发时，少不了对文件的读写操作。
# 在管理多个线程对同一文件的读写操作时，就少不了文件锁了。

# ######################################################################################################################
# 同步锁(Lock)
# ######################################################################################################################

# 代码案例1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time
import threading

def addNum():
    global num  # 在每个线程中都获取这个全局变量
    num -= 1

num = 100  # 设定一个共享变量
thread_list = []

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()
print('Result: ', num)

# ==================================
# Result:  0

# 代码案例2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time
import threading

def addNum():
    global num  # 在每个线程中都获取这个全局变量
    temp = num
    time.sleep(1)
    num = temp - 1  # 对此公共变量进行-1操作

num = 100  # 设定一个共享变量
thread_list = []

for i in range(100):  # 循环进行了100次addNum函数
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)
for t in thread_list:  # 等待所有线程执行完毕
    t.join()
print('Result: ', num)

# ============================
# Result:  99

# 100个线程同时竞争运行函数，睡眠1s肯定够100个进程运行到同时处于睡眠的状态，
# 第一个竞争到的肯定率先醒来速度极快计算完，num=99，线程2醒来从上面携带的global num=100同样计算num=99

# 代码案例3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time
import threading

def addNum():
    global num  # 在每个线程中都获取这个全局变量
    temp = num
    time.sleep(0.001)
    num = temp - 1  # 对此公共变量进行-1操作

num = 100  # 设定一个共享变量
thread_list = []

for i in range(100):  # 循环进行了100次addNum函数
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('Result: ', num)

# ============================
# Result: 93或91或89...

# 每次执行程序结果都不同。100个线程因为GIL大锁的原因竞争运行函数，for循环第一次时线程1率先运行函数，
# 线程1最快运行到time.sleep(0.001)睡眠时，GIL释放，线程1还未运行完addNum函数。
# for循环了2,3...次，线程2，3...竞争到运行函数，
# 假设线程1 醒来时不知道有多少个线程在同时运行函数，当线程1计算num值，num值改变了，
# 改变后的num值对在函数中的线程2,3...计算时num已经不是100的初始值了，num值由于一直不停的有线程进入一直在改变。
# 而且线程1睡眠时不知道有多少个线程同时在睡眠，最后的结果肯定也不同。

# 同步锁(Lock)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 上述就是线程安全问题，数据不可控，不安全，解决方法就是再创建一把锁。
# 锁通常被用来实现对共享资源的同步访问。 为每一个共享资源创建一个Lock对象，
# 当你需要访问该资源时，调用acquire方法来获取锁对象（如果其它线程已经获得了该锁，则当前线程需等待其被释放），
# 待资源访问完后，再调用release方法释放锁：
# 注意获取锁和释放锁的位置
import time
import threading

def addNum():
    global num
    lock.acquire()  # 获取这把锁
    temp = num
    time.sleep(0.01)
    num = temp - 1
    lock.release()  # 释放这把锁

num = 100
thread_list = []
lock = threading.Lock()  # 创建一把锁

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()
print('Result: ', num)

# ==================================
# Result:  0

# ######################################################################################################################
# 互斥锁介绍
# ######################################################################################################################
# 当多个线程共享一个数据的时候，必须要进行同步的控制，不然会出现不可预期的结果，即 “线程不安全”

# 互斥锁介绍~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。
互斥锁为资源引入一个状态：锁定/非锁定。
某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；
直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。
互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
'''

# threading模块中定义了Lock类，可以方便的处理锁定：
import threading
# 创建锁
mutex = threading.Lock()
# 锁定
mutex.acquire([timeout])
# 解锁
mutex.release()

# 互斥锁案例~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import threading
import time

def writetoTxt(txtFile):
    id = threading.currentThread().getName()
    mutex.acquire(10)
    with open(txtFile, 'a') as f:
        print("Thread {0} acquire lock".format(id))
        f.write("write from thread {0} \r\n".format(id))
        time.sleep(3)
    mutex.release()
    print("Thread {0} exit".format(id))

mutex = threading.Lock()

for i in range(5):
    myThread = threading.Thread(target=writetoTxt, args=("test.txt",))
    myThread.start()

# 当一个线程调用锁的acquire()方法获得锁时，锁就进入“locked”状态。每次只有一个线程可以获得锁。
# 如果此时另一个线程试图获得这个锁，该线程就会变为“blocked”状态，称为“同步阻塞”。
# 直到拥有锁的线程调用锁的release()方法释放锁之后，锁进入“unlocked”状态。
# 线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。

# ######################################################################################################################
# 使用fcntl（只有Linux系统可以用）
# ######################################################################################################################

# fcntl方法介绍~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
在linux下，python的标准库有现成的文件锁，来自于fcntl模块。这个模块提供了unix系统fcntl()和ioctl()的接口。
对于文件锁的操作，主要需要使用 fcntl.flock(fd, operation)这个函数。
其中，参数 fd 表示文件描述符；参数 operation 指定要进行的锁操作，该参数的取值有如下几种：
LOCK_SH：表示要创建一个共享锁，在任意时间内，一个文件的共享锁可以被多个进程拥有
LOCK_EX：表示创建一个排他锁，在任意时间内，一个文件的排他锁只能被一个进程拥有
LOCK_UN：表示删除该进程创建的锁
LOCK_MAND：它主要是用于共享模式强制锁，它可以与 LOCK_READ 或者 LOCK_WRITE联合起来使用，
从而表示是否允许并发的读操作或者并发的写操作
'''

# fcntl方法案例~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
import fcntl
import threading
import time

def writetoTxt(txtFile):
   id = threading.currentThread().getName()
   with open(txtFile, 'a') as f:
       fcntl.flock(f.fileno(), fcntl.LOCK_EX) #加锁
       print "{0} acquire lock".format(id)
       f.write("write from {0} \r\n".format(id))
       time.sleep(3)
   # 在with块外，文件关闭，自动解锁
   print "{0} exit".format(id)

for i in range(5):
    myThread = threading.Thread(target=writetoTxt, args=("test.txt",))
    myThread.start()
'''
# 代码运行期间，控制台将依次打印哪个线程获得了锁，在对文件进行读写。
# 通过调用 fcntl.flock(f.fileno(), fcntl.LOCK_EX) 对文件加锁，如果有其他线程尝试对test文件加锁，会被阻塞。
# 当线程执行完毕的时候，锁会自动释放。或者也可以采取主动的方式解锁：调用fcntl.flock(f.fileno(),
# fcntl.LOCK_UN)函数，对文件test解锁

