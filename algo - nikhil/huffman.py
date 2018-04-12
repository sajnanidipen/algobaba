class HuffNode :
    def __init__(self,c,f):
        self.char=c
        self.freq=f
        self.left = None
        self.right=None

class HuffList :
    def __init__(self):
        self.hufflist = []        
    def insert(self, cf):        
        if len(self.hufflist)==0 :
            self.hufflist.append(cf)
        else:
            i=0
            n =len(self.hufflist)
            while (i<n):
                if(self.hufflist[i].freq> cf.freq):
                    break
                i = i +1                         
            self.hufflist.insert(i,cf)
        
    def makeList(self,strdata):
        n=len(strdata)
        i=0
        while( i<n):            
            if(strdata[i]!="-"):
                count=strdata.count(strdata[i])                
                c = HuffNode(strdata[i], count)                
                self.insert(c)
                strdata = strdata.replace(strdata[i],"-")                
            i = i + 1
            
    def printList(self) :
        for x in self.hufflist :
            print(x.char , ":" , x.freq)

    def makeTree(self):                
        while (len(self.hufflist)!=1) :
            min1index = 0
            min2index = 1
            node1 = self.hufflist.pop(0)
            node2 = self.hufflist.pop(0)
            newnode = HuffNode(node1.char+node2.char, node1.freq + node2.freq)
            newnode.left = node1
            newnode.right= node2
            self.insert(newnode)
                      
    def postorder(self,node,code):        
        if (node is not None) :              
            self.postorder(node.left, code + "0")
            self.postorder(node.right, code + "1") 
            if(len(node.char)==1):
                print(node.char ,":", code)
              
x = HuffList()
x.makeList("this is it and it is great")
x.printList()
x.makeTree()
x.printList()
x.postorder(x.hufflist[0],"")
