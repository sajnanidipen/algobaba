class BSTree:
    def __init__(self):
        self.root=None
    def insertNode(self,root,node):
        if self.root is None:
            self.root =node
        else:
            if root.data> node.data:
                if root.left==None:
                    root.left=node
                else:
                     self.insertNode(root.left,node)
            elif root.data< node.data:
                if root.right==None:
                    root.right=node
                else:
                    self.insertNode(root.right,node)
    def preorder(self,node):
         if(node!=None):
              print(node.data)
              self.preorder(node.left)
              self.preorder(node.right)
    def locate(self,x):
           if self.root.data==x.data:
               loc=self.root.data
               parent=None
               return [parent,loc]
           else:
               found=False
               if x.data<self.root.data:
                   loc=self.root.left
                   parent=self.root
               else:
                   loc=self.root.right
                   parent=self.root
                   while(loc!=None and not found):
                       if(x.data==loc.data):
                           found=True
                       elif (x.data<loc.data):
                           parent=loc
                           loc=loc.left
                       else:
                           parent=loc
                           loc=loc.right
           return [parent.data,loc.data]             
                
class BSTNode:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
   

Kroot=None
D=BSTNode("D")
A=BSTNode("A")
E=BSTNode("E")
B=BSTNode("B")
tree1=BSTree()
tree1.insertNode(tree1.root,D)
tree1.insertNode(tree1.root,A)
tree1.insertNode(tree1.root,B)
tree1.insertNode(tree1.root,E)
tree1.preorder(D)
print(tree1.locate(E))







