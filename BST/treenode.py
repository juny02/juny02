class TreeNode:
    def __init__(self, leaf=False):
        self.leaf=leaf
        self.keys=[]
        self.keyLen=len(self.keys)
        if leaf:
            self.value=[] #key, value pair
            self.right=None
        else:
            self.child=[]
            self.rightChild=None

class B_Plus_Tree:
    def __init__(self, m):
        self.root = TreeNode(leaf=True)
        self.m=m
    def search(self, target): #이진탐색과 같은 알고리즘. 한번 탐색하면 그반대방향애들과는 탐색할 필요가 없어짐 !
        cur=self.root
        while cur:
            if cur.key==target:
                return cur
            elif cur.key<target:
                cur=cur.right
            else:
                cur=cur.left
        return cur #못찾으면 cur이 끝까지 = None까지 가므로 이런 설정 해둔 것