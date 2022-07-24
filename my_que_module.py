class my_que:
    # 이 자료구조는 링버퍼큐 이며 큐의 최대크기를 미리 설정함에 따라서 메모리를 최소화하려는 의도에따라 코드를 작성함.
    def __init__(self, length):
        self.length = length
        self.arr = [None] * length
        self.front = 0
        self.rear = 0
        self.cnt = 0

    #컨테이너가 비어있는지확인
    def is_empty(self):
        if self.cnt == 0:
            return True
        else:
            return False

    #컨테이너가 가득차있는지 확인
    def is_full(self):
        if self.cnt == self.length:
            return True
        else:
            return False

    def enque(self, value):
        if self.is_full():
            print("que is full")
            return -1
        if self.rear == self.length - 1:
            self.arr[self.rear] = value
            self.rear = 0
            self.cnt += 1
        else:
            self.arr[self.rear] = value
            self.rear += 1
            self.cnt += 1

    def deque(self):
        if self.is_empty():
            print("empty")
            return -1
        if self.front == self.length - 1:
            tmp = self.arr[self.front]
            self.front = 0
            self.cnt -= 1
            print(tmp, 'has been dequeued.')
            return tmp
        else:
            tmp = self.arr[self.front]
            self.front += 1
            self.cnt -= 1
            print(tmp, 'has been dequeued.')
            return tmp


if __name__ == "__main__":
    a = my_que(10)
    a.enque(1)
    a.enque(2)
    a.enque(3)
    a.enque(4)
    a.enque(5)
    a.enque(6)
    a.enque(7)
    a.enque(8)
    a.enque(9)
    a.enque(10)
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.enque(11)
    a.enque(12)
    a.enque(13)
    a.enque(14)
    a.enque(15)
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    a.deque()