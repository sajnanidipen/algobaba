class Quicksortalgo:
    def __init__(self, arr):
        self.list1=arr

    def quicksort(self):
        self.quicksorthelper(0, len(self.list1)-1)
        
    def quicksorthelper(self, low, high):
        if low<high:
            pi=self.partition(low,high)
            self.quicksorthelper(low,pi-1)
            self.quicksorthelper(pi+1,high)
            
    def partition(self, low,high):
        i=(low-1)
        pivot=self.list1[high]
        for j in range(low,high+1):
            if self.list1[j]<=pivot:
                i=i+1
                self.list1[i],self.list1[j]=self.list1[j],self.list1[i]
        return i
    
#arr=[10,7,8,9,1,5]
arr=[x for x in input("Enter numbers: ").split(" ")]
print(arr)
for i in arr:
    i = int(i)
a  = Quicksortalgo(arr)
a.quicksort()
print("Sorted Analysis")
for i in arr:
    print(i)
