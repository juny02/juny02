class Stack:
    def __init__(self):
        self.container=list() #비어있는 리스트 생성하기

    def empty(self):
        if not self.container: #비어있는 리스트 자체 = false 이므로
            return True
        else:
            return False

    def push(self,data):
        self.container.append(data)

    def pop(self):
        if self.empty():
            return None
        return self.container.pop() #pop이 원래 반환함 !

    def peek(self):
        if self.empty():
            return None
        return self.container[-1] #마지막 요소 !!

s = Stack()
for i in range(1,6):
    s.push(i)

print(s.peek())

while not s.empty():
    print(s.pop(), end=' ')