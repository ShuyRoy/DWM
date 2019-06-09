class Graph:
    def __init__(self,val):
        self.node_id = 0
        self.node = {self.node_id:val}  #保存节点的值
        self.edge = {self.node_id:[]}
    def insert(self,val,L1,L2):    #L1存的该节点指向谁，L2存的是谁指向该节点
        self.node_id += 1
        self.node[self.node_id] =val   #保存节点记录的值
        for e in L2:
            self.edge[e].append(self.node_id)   #更新边的信息
        self.edge[self.node_id] = L1
    def exist_val(self,val):
        value = self.node.values()      #value为字典中的所有值组成的列表
        return val in value
    def show(self):
        print("节点的信息",self.node)
        print("边的信息",self.edge)
