from random import randint

def create_array():
    return [randint(0,10) for i in range(10)]

def quicksort(a):
    if len(a) <=1:
        return a

    smaller=[]
    equal=[]
    larger=[]

    pivot = a[randint(0,len(a)-1)]

    for x in a:
        if(x<pivot):
            smaller.append(x)
        elif(x==pivot):
            equal.append(x)
        else:
            larger.append(x)

    return quicksort(smaller)+equal+quicksort(larger)

a=create_array();
print("Before Sorting...",a)
s=quicksort(a)
print("After Sorting...",s)
