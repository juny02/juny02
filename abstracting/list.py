class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        print("세터!")
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

class DoubledLinkedList:
    #head, tail은 비어있는 것 !
    def __init__(self):
        self.head=Node()
        self.tail=Node()

        self.head.next=self.tail
        self.tail.prev=self.head

        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add_first(self, data):
        add=Node(data)

        add.prev=self.head
        add.next=self.head.next

        self.head.next.prev=add
        self.head.next = add # 순서 꼭 이렇게 해야함 !!

        self.d_size+=1

    def add_last(self, data):
        add=Node(data)

        add.prev=self.tail.prev
        add.next=self.tail

        self.tail.prev.next=add
        self.tail.prev=add

        self.d_size+=1

    def insert_after(self, n, data):
        add=Node(data)
        k=self.head
        for i in range(0, n):
            k=k.next

        add.prev=k
        add.next=k.next

        k.next.prev=add
        k.next=add

        self.d_size+=1





a=[3,2,1,7,8]
print(a[1:])




