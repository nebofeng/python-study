#保留有限历史记录正是 collections.deque

from collections import deque

#deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉
# deque 学习： https://www.cnblogs.com/zhenwei66/p/6598996.html

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'D:\data\test.txt') as f:
        print(list(search(f, 'python', 5)))
        #print(list(search(f, 'python', 5)))
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

