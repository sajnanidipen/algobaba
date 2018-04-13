class vertex:
    def __init__(self,v):
        self.node=v
        self.visited=False
    def  setvertex(self,v):
        self.node=v      
    def  getvertex(self):
        return self.node
    def visited (self,b):
        self.node=b
class Mygraph:
    def __init__(self):
        self.nodes=[]
        self.adjacency=[]
        self.first=None
        self.second=None
    def getnodes(self):
        return self.nodes
    def PutNone(self):
        for i in range(len(self.nodes)):
            a=[]
            for i in range(len(self.nodes)):
                a.append(None)
            self.adjacency.append(a)
    def addnode(self,d):
        self.nodes.append(d)
        
    def getID(self):
        for i in range(len(self.nodes)):
                print(self.nodes[i].node)
        
    def addedge(self,g):
        self.first=g[0]
        self.second=g[1]
        id1=None
        id2=None
        for i in range(len(self.nodes)):
            if (self.first==self.nodes[i].node):
                id1=i
                print(id1)
                break
        for i in range(len(self.nodes)):
            if (self.second==self.nodes[i].node):
                id2=i
                break
        
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if(id1==i and id2==j):
                    self.adjacency[i][j]=1
                elif(self.adjacency[i][j]==1):
                     self.adjacency[i][j]=1
                else:
                   self.adjacency[i][j]=0
                   
        
                   
    def printmatrix(self):
        print(self.adjacency)            

g1=Mygraph()
i=int(input("Enter No of vertex:"))
for j in range(i):
    A=vertex(str(input("Enter  vertex:")))
    g1.addnode(A)
g1.PutNone()
for i in range(4):
    r=str(input("Eneter Edge:"))
    g1.addedge(r)
g1.printmatrix()

        
        
