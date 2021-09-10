'''
2. 원형 큐로 구현하기 !
- dequeue(데이터빼기)할 때, front만 움직이면됨
- rear은 마지막데이터 다음을 가리킴
- rear가 맨 마지막에 도달하면, 동적배열의 처음 가리키게 하면 됨 !
'''

class CQueue:
    MAXSIZE = 10
    def __init__(self):
        self.container=[None for _ in range(self.MAXSIZE)]
        self.front=0
        self.rear=0

    def is_empty(self):
        if self.front==self.rear:
            return True
        else:
            return False

    def __step_forward(self,x):
        x+=1
        if x>=CQueue.MAXSIZE:
            x=0
        return x

    def is_full(self):
        next=self.__step_forward(self.rear)
        if self.front==next:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        self.container[self.rear]=data
        self.rear=self.__step_forward(self.rear)

    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        a=self.container[self.front]
        self.front=self.__step_forward(self.front)
        return a

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        return self.container[self.front]

cq=CQueue()
for i in range(8):
    cq.enqueue(i)

for i in range(10):
    print(cq.container[i], end=' ')

for i in range(5):
    cq.dequeue()

print()
for i in range(10):
    print(cq.container[i], end=' ')

for i in range(8, 14):
    cq.enqueue(i)

print()
def printq():
    if cq.front>cq.rear:
        for i in range(cq.front, cq.MAXSIZE):
            print(cq.container[i], end=' ')
        for i in range(0,cq.rear):
            print(cq.container[i], end=' ')
    else:
        for i in range(cq.front,cq.rear):
            print(cq.container[i], end=' ')
    print()

printq()

cq.dequeue()
printq()

print()
print(cq.front, cq.rear)

print(cq.is_empty())
