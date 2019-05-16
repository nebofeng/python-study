import threading

def fun1(a):
    print(a)

def fun2(a):
    print(a.isAlive())
    a.is_alive


if __name__ == "__main__":
    fun1(12)
   # fun2(22)
    t1=threading.Thread(target=fun1,args=(1,))
    t1.start()
    print(t1.is_alive)
    t2=threading.Thread(target=fun2,args=(t1,))
    t2.start()

