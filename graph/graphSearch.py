from queue import Queue
from stack import Stack

#그냥 단순 그래프
class Graph:
    def __init__(self,vertex_num):
        self.adj_list=[[]for _ in range(vertex_num)]

        self.visited=[False for _ in range(vertex_num)]

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def init_visted(self): #방문 여부 초기화 함수
        for i in range(len(self.visited)):
            self.visited[i]=False

    def bfs(self, v):
        self.init_visted()
        q=Queue()
        q.put(v)
        self.visited[v]=True

        while not q.empty():
            v=q.get()
            print(v)
            adj=self.adj_list[v]
            for i in adj:
                if not self.visited[i]:
                    q.put(i)
                    self.visited[i]=True
    #재귀함수-스택프레임 이용
    def __dfs_recursion(self, v):
        print(v, end=' ')
        self.visited[v] = True

        adj=self.adj_list[v]
        for i in adj:
            if not self.visited[i]:
                self.__dfs_recursion(i)

    def dfs(self,v):
        self.init_visted()
        self.__dfs_recursion(v)

    #스택 자료구조 이용
    def iter_dfs(self,v):
        s=Stack()
        self.init_visted()

        s.push(v)
        self.visited[v]=True
        print(v)

        while not s.empty():
            find = False
            adj=self.adj_list[s.peek()]
            for i in adj:
                if not self.visited[i]:
                    self.visited[i]=True
                    s.push(i)
                    print(i)
                    find=True
                    break
            if not find:
                s.pop()

            '''
            포문 안에서 인접한 값을 찾음 -> find값 true! 다음 서치도 할 수 있다
            그러나 포문안에서 인접값 못찾음->요값은 끝낫다! find값이 false로 그대로니까 pop 시켜버림
            '''

a=Graph(4)
a.add_edge(0,1)
a.add_edge(1,2)
a.add_edge(2,3)

a.iter_dfs(2)
