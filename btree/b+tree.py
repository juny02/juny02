import math
from queue import Queue
import csv

class TreeNode:
    def __init__(self, leaf=False):
        self.leaf=leaf
        self.keys=list()
        self.keyLen=len(self.keys)
        self.parent=None
        if leaf:
            self.value=dict()
            self.right=None
        else:
            self.child=dict()
            self.rightChild=None

class B_Plus_Tree:
    def __init__(self, m):
        self.root = TreeNode(True)#(leaf=True)
        self.m=m

    def find_first_node(self, target):
        cur = self.root
        while not cur.leaf:
            index=-1
            find = False
            for i in range(len(cur.keys)):
                if cur.keys[i] >= target:
                    find = True
                    index=i
                    break
            if not find:
                cur = cur.rightChild
            elif cur.keys[index] > target: #찾음
                cur = cur.child[cur.keys[i]]
            else:
                if len(cur.keys) == i+1:
                    cur = cur.rightChild
                else:
                    cur = cur.child[cur.keys[i+1]]
        return cur

    def Search(self, target):
        cur=self.find_first_node(target)

        for i in range(len(cur.keys)):
            if cur.keys[i]==target:
                return cur.value[cur.keys[i]]

    def RangedSearch(self,start, end):
        cur1=self.find_first_node(start)
        key1=0
        for i in range(len(cur1.keys)): #정렬 처음 노드찾음
            if cur1.keys[i] >= start:
                key1=cur1.keys[i]
                break

        find=False
        cur2=self.find_first_node(end)
        key2=0
        for i in range(len(cur2.keys)): #마지막 노드 찾음
            if cur2.keys[i]==end:
                key2=cur2.keys[i]
                find=True
                break
            elif cur2.keys[i]>end:
                key2=cur2.keys[i-1]
                find=True
                break
        if not find:
            key2=cur2.keys[len(cur2.keys)-1]

        cur=cur1
        keys=cur.keys
        finish=False
        result=list()
        while True:
            for k in keys:
                if key1<=k<=key2:
                    result.append(cur.value[k])
                if k>key2:
                    finish=True
            if finish:
                break #끝나면 바로 나가라고 해둔것
            elif not cur.right:
                break
            cur=cur.right
            keys = cur.keys
        return result

    def insert_leaf(self, node, pair):
        n=0
        for i in range(len(node.keys)):
            if node.keys[i]>pair[0]:
                node.keys.insert(i, pair[0])
                n=1
                break
        if n==0:
            node.keys.append(pair[0])
        node.value[pair[0]] = pair[1]


    def insert_index(self, node, key, left, right):
        index=0
        last=True
        for i in range(len(node.keys)):
            if node.keys[i]>key:
                node.keys.insert(i, key)
                index = i
                last=False
                break
        if last:
            node.keys.append(key)

        node.child[key]=left
        if node.keys[-1]==key :#마지막 요소라면
            node.rightChild=right
        elif node.keys[0]==key: #맨처음요소라면
            node.child[node.keys[i+1]]=right
        else: #중간이면
            nextKey=node.keys[i+1]
            node.child[nextKey]=right

        left.parent=node
        right.parent=node

    def Insert(self,pair): #pair 은 키, 벨류의 쌍
        node=self.find_first_node(pair[0])
        self.insert_leaf(node,pair)
        if len(node.keys)==self.m: #넘쳤으면
            self.split(node)




    def split(self, node):
        k=math.ceil((self.m+1)/2)-1
        split_key=node.keys[math.ceil((self.m+1)/2)-1]
        parent = node.parent
        node1= None
        node2 = None
        if node.leaf:
            node2 = TreeNode(True)
            node2.keys=node.keys[k:]
            node2.right=node.right
            for i in node2.keys:
                node2.value[i]=node.value[i]
            copydict=node.value
            node.child=dict()
            node.keys = node.keys[:k]
            node.right = node2
            for i in node.keys:
                node.value[i]=copydict[i]

        else: #자식이 리프면, 두개 이어주는거 하기 !!!!
            node1 = TreeNode()
            node2 = TreeNode()
            node1.keys = node.keys[:k]
            node2.keys = node.keys[k+1:]
            for i in node1.keys:
                node1.child[i]=node.child[i]
                node1.child[i].parent=node1
            node1.rightChild=node.child[split_key]
            node1.rightChild.parent=node1
            for i in node2.keys:
                node2.child[i]=node.child[i]
                node2.child[i].parent=node2
            node2.rightChild=node.rightChild
            node2.rightChild.parent=node2


        if node==self.root: #쪼개야 하는 노드가 루트면?
            root=TreeNode()
            if node.leaf:
                node.parent=root
            else:
                node1.parent=root
            node2.parent=root
            parent=root
            self.root=root

        if node.leaf:
            self.insert_index(parent, split_key, node, node2)
        else:
            self.insert_index(parent, split_key, node1, node2)


        if len(parent.keys)==self.m: #부모가 넘쳤으면

            parent = self.split(parent)

    def printTree(self):
        q = Queue()
        cur=self.root
        q.put(cur)
        print(cur.keys, end=' ')
        cur = q.get()
        print()
        while not cur.leaf:
            for k in cur.keys:
                print(cur.child[k].keys, end=' ')
                q.put(cur.child[k])

            print(cur.rightChild.keys, end=' ')
            print('이 노드 끝',end =' ')
            q.put(cur.rightChild)
            if not cur.rightChild.leaf:
                print('')
            cur = q.get()



#for text, 노가다 b+ 구현
'''
t=B_Plus_Tree(3)
t.root.keys.append(5)

d=TreeNode(True)
d.keys.append(7); d.keys.append(8)
d.value[7]='7입니다'
d.value[8]= '8입니다'

c=TreeNode(True)
c.keys.append(5); c.keys.append(6)
c.value[5]='5입니다'
c.value[6]='6입니다'
c.right=d

b=TreeNode(True)
b.keys.append(3) ; b.keys.append(4)
b.value[3]='3입니다'
b.value[4]='4입니다'
b.right=c

a=TreeNode(True)
a.keys.append(1) ; a.keys.append(2)
a.value[1]='1입니다'
a.value[2]='2입니다'
a.right=b

a1=TreeNode()
a1.keys.append(3)
a1.child[3]=a
a1.rightChild=b
a1.parent=t.root

b1=TreeNode()
b1.keys.append(7)
b1.rightChild=d
b1.child[7]=c
b1.parent=t.root

a.parent=a1
b.parent=a1
c.parent=b1
d.parent=b1


t.root.rightChild=b1
t.root.child[5]=a1

print('***********start*************')
t.printTree()
print()
print('************end**************')

t.Insert([5.5, '5.5입니다'])
print('***********start*************')
t.printTree()
print()
print('************end**************')

t.Insert([9, '9입니다'])
print('***********start*************')
t.printTree()
print()
print('************end**************')

t.Insert([2.2, '2.2입니다'])
print('***********start*************')
t.printTree()
print()
print('************end**************')

t.Insert([0, '0입니다'])
print('***********start*************')
t.printTree()
print()
print('************end**************')

t.Insert([3.3, '3.3입니다'])
print('***********start*************')
t.printTree()
print()
print('************end**************')
'''




f=open('input.csv', 'r')
tree=B_Plus_Tree(4)
rdr=csv.reader(f)
for line in rdr:
    tree.Insert([int(line[0]),line[1]]) #포인터를 어캐할건지 생각하세요
f.close()

print('***********start*************')
tree.printTree()
print()
print('************end**************')

print(tree.Search(37))







