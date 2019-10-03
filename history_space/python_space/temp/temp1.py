import numpy
def func1(x):
    if(len(str(x)) != 4):
        print('请输入4位数字')
    else:
        a = int(((x+5) / 1) % 10)
        b = int(((x+50) / 10) % 10)
        c = int(((x+500) / 100) % 10)
        d = int(((x+5000) / 1000) % 10)
        y = a*1000 + b*100 + c*10 + d*1
        # print(a,b,c,d)
        return y


def func2(x):
    x.sort(reverse=True)
    y = x[0] + x[1]
    return y

a = [1,2,3]
func2(a)
