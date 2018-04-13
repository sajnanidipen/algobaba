class Tree1:
    def __init__(self,d):
        self.data=d
        self.lchild=None
        self.rchild=None
class MyTree:
    def __init__(self,t):
        self.root=t
    def postorder(self,t):
        if t is not None:
            self.postorder(t.lchild)
            self.postorder(t.rchild)
            print(t.data)
A=Tree1("A")
B=Tree1("B")
C=Tree1("C")
D=Tree1("D")
E=Tree1("E")
F=Tree1("F")
A.lchild=B
A.rchild=C
B.lchild=D
B.rchild=E
C.rchild=F
mt=MyTree(A)
print("The postorder traversal is:")
mt.postorder(mt.root)
