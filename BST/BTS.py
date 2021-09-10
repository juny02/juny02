from treenode import TreeNode

class BTS:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, func):
        if not cur:
            return

        func(cur)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    def inorder_traverse(self, cur, func):
        if not cur:
            return

        self.inorder_traverse(cur.left, func)
        func(cur)
        self.inorder_traverse(cur.right, func) #탐색

    #편의 함수
    #cur의 왼쪽 자식을 (입력받은)left로 만든다
    def __make_left(self,cur,left):
        cur.left=left
        if left: #논이면, 이런거 설정할 필요 없으니까 !
            left.parent = cur

    #cur의 오른쪽 자식을 입력받은 애로 만든다
    def __make_right(self,cur, right):
        cur.right=right
        if right:
            right.parent=cur

    def insert(self, key):
        '''
        부모에서 쭉 크기 비교하면서 빈자리찾아서 감
        (만난거랑 넣을거랑 비교햇을때, 넣을게 크면 오른쪽으로, 작으면 왼쪽으로감 )
        '''
        new=TreeNode(key)

        cur=self.root()
        if not cur:
            self.root=new
            return

        while True:
            parent=cur
            if cur.key>key:
                cur=cur.left
                if not cur:
                    self.__make_left(parent, new)
                    return
            else:
                cur=cur.right
                if not cur:
                    self.__make_right(parent, new)
                    return

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

    def __delete_recursion(self, cur, target):
        if not cur:
            return None #cur끝까지 갓는데 target값없이 그냥 none까지 간 경우/ 걍 시작노드(cur)에 none이 제시된 경우
        elif cur.key>target:
            new_left=self.__delete_recursion(cur.left,target)


    def min(self, cur):
        while cur.left != None: #굿아이디어
            cur=cur.left
        return cur
    def max(self,cur):
        while cur.right !=None:
            cur.right
        return cur

    def prev(self, cur): #해당 노드의 키보다 하나 작은거 찾는 함수
        if cur.left:
            return self.max(cur.left)

        parent=cur.parent
        while parent and parent.left==cur: #parent가 none일 수도 있으므로 !!
            cur=parent
            parent=parent.parent

        return parent

    def next(self, cur): #해당노드의 키보다 하나 큰 노드 찾는 함수
        if cur.right:
            return self.min(cur.right)
        
        parent=cur.parent
        while parent and parent.right==cur:
            cur=parent
            parent=parent.parent
        return parent


