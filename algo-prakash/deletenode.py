class BSNode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def getLeft():
        return self.left
    def getRight():
        return self.data
class BSTree:
    def __init__(self):
        self.root=None
    def insertNode(self,root,node):
        if (self.root==None):
            self.root=node
            #print("Address of "+str(self.root.data)+" "+str(self.root))    
        else:
            if(root.data>node.data):
                if (root).left==None:
                    (root).left=node
                    print("Address of "+str(root.left.data)+" "+str(root.left))
                else:
                    self.insertNode(root.left,node)
            else:
                if (root).right==None:
                    (root).right=node
                    print("Address of "+str(root.right.data)+" "+str(root.right))
                else:
                    self.insertNode(root.right,node)
    def preorderTraversal(self,node):
        if (node!=None):
            print(node.data)
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)
    def locate(self,x):
        if(self.root.data==x):
            loc=self.root
            parent=None
            return [loc,parent]
        else:
            found=False
            if (x<self.root.data):
                loc=self.root.left
            else:
                loc=self.root.right
            parent=self.root
            while(loc!=None and not found):
                if(x==loc.data):
                    
                    found=True
                elif (x<loc.data):
                    parent=loc
                    loc=loc.left
                else:
                    parent=loc
                    loc=loc.right
                return [parent,loc]
    def deleteNode(self,obj,x):
        pos=self.locate(x)
        if(pos[1].left==None and pos[1].right==None):
            obj.setData(None);
            
        
                    
                

        
D=BSNode("D")
A=BSNode("A")
F=BSNode("F")
B=BSNode("B")
Tree=BSTree()
Tree.insertNode(Tree.root,D)
Tree.insertNode(Tree.root,A)
Tree.insertNode(Tree.root,B)
Tree.insertNode(Tree.root,F)
print("Preorder Traversal")
Tree.preorderTraversal(D)
print(Tree.deleteNode(B,"B"))
Tree.preorderTraversal(D)
