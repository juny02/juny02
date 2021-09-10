# 1. 동적배열로 구현
class Queue:
    def __init__(self):
        self.container=list()

    def is_empty(self):
        if not self.container:
            return True
        else:
            return False

    # def is_full(self): ?

    def enqueue(self,data):
        self.container.append(data)

    def dequeue(self):
        return self.container.pop(0) #이게 효율적이지 X !

    def peek(self):
        return self.container[0]