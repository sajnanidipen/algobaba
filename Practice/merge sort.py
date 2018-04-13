#from random import randint
def merge(left,right):
    result = []
    i,j = 0,0
    while(i<len(left) and j<len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result += left[i:]
    result += right[j:]
    return result

def mergesort(lst):
    if (len(lst) <= 1):
        return lst
    mid = int(len(lst)/2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left,right)

#a=[randint(0,10) for i in range(10)]
arr=[]
x=0
num=int(input("Enter No. of Elements in Array:"))
for i in range(num):
    x=int(input("Enter the Elements:"))
    arr.append(x)
print("Before Sorting...",arr)

print("After Sorting...",mergesort(arr))
