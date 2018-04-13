class mergesort:
   def __init__(self):
      self.listOfLists = []
   def mergeSortAlgorithm(self,x):

       for i in range(len(x)):
           temp = [x[i]]
           self.listOfLists.append(temp)
       while(len(self.listOfLists) != 1):
           j = 0
           while(j < len(self.listOfLists)-1):
               tempList = self.merge(self.listOfLists[j], self.listOfLists[j+1])
               self.listOfLists[j] = tempList
               del self.listOfLists[j+1]
       print(self.listOfLists[0], "is sorted!")

   def merge(self,a, b):
      newList = []
      count1, count2 = 0, 0
      while((count1 < len(a)) and (count2 < len(b))):
         if(a[count1] > b[count2]):
            newList.append(b[count2])
            count2 = count2 + 1

         elif(a[count1] < b[count2]):
            newList.append(a[count1])
            count1 = count1 + 1

         elif(a[count1] == b[count2]):
            newList.append(a[count1])
            newList.append(b[count2])
            count1, count2 = count1 + 1, count2 + 1

      if(count1 < len(a)):
         for f in range(count1, len(a)):
               newList.append(a[f])
      elif(count2 < len(b)):
         for k in range(count2, len(b)):
               newList.append(b[k])

      return newList
n=int(input("enter length of list:"))
arr=[]
for i in range(0,n):
   arr.append(int(input()))
m=mergesort()
m.mergeSortAlgorithm(arr)
