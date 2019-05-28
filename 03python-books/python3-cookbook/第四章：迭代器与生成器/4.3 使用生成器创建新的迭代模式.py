# 如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。 下面是一个生产某个范围内浮点数的生成器：

#https://www.runoob.com/w3cnote/python-yield-used-analysis.html
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))


# yield 关键字：返回当前的，


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
     yield n
     n -= 1
    print('Done!')

# Create the generator, notice no output appears
c = countdown(3)

# Run to first yield and emit a value
next(c)
# Run to the next yield
next(c)
# Run to next yield
next(c)

# Run to next yield (iteration stops)


#输出斐波那契數列前 N 个数
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)


#文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。好的方法是利用固定长度的缓冲区来不断读取文件内容。
# 通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return