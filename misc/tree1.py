class TreeNode:
    def __init__(self,d):
        self.data=d
        self.lchild=None
        self.rchild=None
class MyTree:
    def __init__(self,t):
        self.root=t
    def preorder(self,t):
        if t is not None:
            print(t.data)
            self.preorder(t.lchild)
            self.preorder(t.rchild)
    def inorder(self,t):
        if t is not None:
            self.inorder(t.lchild)
            print(t.data)
            self.inorder(t.rchild)
    def postorder(self,t):
        if t is not None:
            self.postorder(t.lchild)
            self.postorder(t.rchild)
            print(t.data)
F=TreeNode("F")
B=TreeNode("B")
K=TreeNode("K")
A=TreeNode("A")
D=TreeNode("D")
C=TreeNode("C")
G=TreeNode("G")
F.lchild=B
F.rchild=K
B.lchild=A
B.rchild=D
D.lchild=C
K.lchild=G
mt=MyTree(F)
print("The preorder traversal is:")
mt.preorder(mt.root)
print("The inorder traversal is:")
mt.inorder(mt.root)
print("The postorder traversal is:")
mt.postorder(mt.root)
    
