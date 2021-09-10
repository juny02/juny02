from queue import Queue

class TreeNode:
    def __init__(self, data=None):
        self.__data=data
        self.__left=None
        self.__right=None

    def __del__(self):
        print('data{} is deleted'.format(self.__data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data=data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

def levelorder(cur):
    q=Queue()
    q.put(cur)
    print(cur.data, end= ' ')
    while not q.empty():
        get=q.get()
        if get.left:
            print(get.left.data, end=' ')
            q.put(get.left)
        if get.right:
            print(get.right.data, end= ' ')
            q.put(get.right)


a=list()
for i in range(1,8): #7개 (1~7)
    a.append(TreeNode(i))

a[0].left=a[1]; a[0].right=a[2]
a[1].left=a[3]; a[1].right=a[4]
a[2].left=a[5]; a[2].right=a[6]

levelorder(a[0])