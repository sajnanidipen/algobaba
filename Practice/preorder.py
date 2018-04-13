class Tree1:
    def __init__(self,d):
        self.data=d
        self.lchild=None
        self.rchild=None
class MyTree:
    def __init__(self,t):
        self.root=t
    def preorder(self,t):
        if t is not None:
            self.preorder(t.lchild)
            self.preorder(t.rchild)
            print(t.data)
A=Tree1("A")
B=Tree1("B")
C=Tree1("C")
D=Tree1("D")
E=Tree1("E")
A.lchild=B
A.rchild=C
B.rchild=D
C.lchild=E
mt=MyTree(A)
print("preorder is:")
mt.preorder(mt.root)
