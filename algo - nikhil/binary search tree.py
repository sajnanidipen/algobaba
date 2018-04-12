class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BSTree :
    def __init__(self):
        self.root = None

    def insertNode(self, kroot, node):                      
        if kroot is None:
            kroot = node
        else:
            if kroot.data > node.data :
                if kroot.left ==None :
                    kroot.left = node
                else :
                    self.insertNode(kroot.left, node)
            else :
                if kroot.right == None:
                    kroot.right = node
                else:
                    self.insertNode(kroot.right, node)
                    
    
    def preorder(self,node):
        if (node != None) :        
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)


    def locate(self, x):
        if self.root.data ==x:
            loc = self.root
            parent = None
            return [parent, loc]
        else:
            f=False
            if x<self.root.data :
                loc = self.root.left
            else :
                loc = self.root.right

            parent = self.root
            while (loc != None and not f) :
                if x == loc.data :
                    f=True
                elif(x <loc.data):
                    parent = loc
                    loc = loc.left
                else:
                    parent = loc
                    loc = loc.right
            return [parent,loc]

    def delete(self, x):
        x = self.locate(x)
        print("parent :" , x[0].data)
        print("node to be deleted :", x[1].data)

        parentloc = x[0]
        loc = x[1]


    def deleteNode(self, root, data):
        if root.data == data:
            if root.right and root.left :
                [psuc, suc] = self.findmin(root.right, root)
                print("found in order succ & its parent", suc.data , ", ", psuc.data)
                if psuc.left == suc :
                    psuc.left = suc.right
                else:
                    psuc.right = suc.right                
                suc.left = root.left
                suc.right = root.right
                print("returning new successor", suc, " with" , suc.left , " & ", suc.right)
                return suc                
            else:
                if root.left :
                    return root.left
                else:
                    return root.right
        else:
            if root.data > data:
                if root.left :
                    root.left = self.deleteNode(root.left, data)                    
            else:
                if root.right :
                    root.right = self.deleteNode(root.right, data)
        return root

    def findmin(self,root,parent) :
        if root.left :
            return self.findmin(root.left, root)
        else:
            return [parent, root]
    

D = BSTNode("D")
A = BSTNode("A")
F = BSTNode("F")
B = BSTNode("B")
M = BSTNode("M")
O = BSTNode("O")
E = BSTNode("E")
    
tree1 = BSTree()
tree1.root = D
tree1.insertNode(tree1.root, A)
tree1.insertNode(tree1.root, B)
tree1.insertNode(tree1.root, F)
tree1.insertNode(tree1.root, M)
tree1.insertNode(tree1.root, O)
tree1.insertNode(tree1.root, E)
tree1.preorder(tree1.root)
print("Preorder traversal after deletion...")
tree1.root = tree1.deleteNode(tree1.root, "D")
tree1.preorder(tree1.root)
