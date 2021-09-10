from stack import Stack
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

def inorder(cur):
    if not cur:
        return

    inorder(cur.left)
    print(cur.data, end=' ')
    inorder(cur.right)

def iter_inorder(cur):
    s=Stack()
    while True:
        while cur:
            s.push(cur)
            cur=cur.left
        cur=s.pop()
        if not cur:
            break
        print(cur.data, end=' ')
        cur=cur.right

def postorder(cur):
    if not cur:
        return

    postorder(cur.left)
    postorder(cur.right)
    print(cur.data, end=' ')

def iter_postorder(cur):
    s=Stack()

    while True:
        while cur:
            s.push(cur)
            cur=cur.left
        s.pop()



a=list()
for i in range(1,8): #7개 (1~7)
    a.append(TreeNode(i))

a[0].left=a[1]; a[0].right=a[2]
a[1].left=a[3]; a[1].right=a[4]
a[2].left=a[5]; a[2].right=a[6]

postorder(a[0])
print()