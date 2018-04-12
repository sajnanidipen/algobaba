class Mergesort:
    def __init__(self):
        self.nlist = []
    def mergeSort(self,nlist):
        print("Splitting ",nlist)
        if len(nlist)>1:
            mid = len(nlist)//2
            lefthalf = nlist[:mid]
            righthalf = nlist[mid:]

            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)
            i=j=k=0       
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    nlist[k]=lefthalf[i]
                    i=i+1
                else:
                    nlist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                nlist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                nlist[k]=righthalf[j]
                j=j+1
                k=k+1
        print("Merging ",nlist)


m=Mergesort()
nlist=[]
a=int(input("Enter number of elements"))
for i in range(a):
    b=int(input("Enter number"))
    nlist.append(b)
m.mergeSort(nlist)
