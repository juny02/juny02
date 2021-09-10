class Graph:
    def __init__(self, vertex_num=None):
        self.adj_list=[] #인접 리스트
        self.vtx_num=0
        self.vtx_arr=[]

        if vertex_num: #값이 존재한다면
            self.vtx_num=vertex_num
            self.adj_list=[[]for _ in range(vertex_num)] #[]을 반복한다는 뜻 !!
            self.vtx_arr=[True for _ in range(vertex_num)]

    def is_empty(self):
        if self.vtx_num==0:
            return True
        else:
            return False

    def add_vertex(self):
        for i in range(len(self.vtx_arr)):
            if not self.vtx_arr[i]:
                self.vtx_arr[i]=True
                self.vtx_num+=1
                return i

        self.vtx_num+=1
        self.adj_list.append([])
        self.vtx_arr+=True
        return self.vtx_num-1

    def delete_vertex(self, v):
        self.vtx_arr[v]=False #pop 하면 하나씩 끌어와야하므로 시간소모마늠. 그래서 이방식 씀 ! 껏다켯다 ~
        self.vtx_num-=1
        self.adj_list[v]=[]

        for a in self.adj_list:
            for k in a:
                if k==v:
                    a.remove(k)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def delete_dege(self,u,v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def adj(self,v):
        return self.adj_list[v]


a=Graph(5)
a.add_edge(1,2)
a.add_edge(1,3)
a.add_edge(2,0)
a.add_edge(4,2)
print(a.adj_list)
a.delete_vertex(2)
print(a.adj_list)



