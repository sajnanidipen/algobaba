alist = [11,8,5,6,7,20,4,4]
qlist =[]
n=len(alist)

for i in range(0,n):
    qlist.append(i)
print(alist)

while True  :
    if len(qlist) ==2 :
        break
    plist = []
    for i  in range(0,len(qlist),2) :
        if(alist[qlist[i]] >= alist[qlist[i+1]] ):
            plist.append(qlist[i])
        else:
            plist.append(qlist[i+1])
    qlist.clear()
    for i in range(0,len(plist)):
        qlist.append(plist[i])
    print("qlist :", qlist)

if ( alist[qlist[0]] > alist[qlist[1]] ) :
    print("Second largest element is ", alist[qlist[1]], " at ", qlist[1])
else :
    print("Second largest element is ", alist[qlist[0]], " at ", qlist[0])          
