class Strassen:
    def __init__(self):
        self.mat=[]
        self.mat1=[]
        self.a11=[];self.a12=[];self.a21=[];self.a22=[];self.b11=[];self.b12=[];self.b21=[];self.b22=[];self.R=[]
        m=int(input("Enter number of rows"))
        n=int(input("Enter number of columns"))
        for i in range(0,n):
            c=[]
            for j in range(0,n):
                c.append("0")
            self.R.append(c)
        print("R",self.R)
        for i in range(0,m):
            a=[]
            a1=[]
            for j in range(0,n):
                b=int(input("Enter elements of matrix 1"))
                a.append(b)
                c=int(input("Enter elements of matrix 2"))
                a1.append(c)
            self.mat.append(a)
            self.mat1.append(a1)
        print("hhhhhhhhhhh",self.multiply(self.mat,self.mat1))

    def multiply(self,a,b):
        
        
        n=len(a)
        print(n)

        if (n == 1):
            self.R[0][0] = a[0][0] * b[0][0]
            return [self.R[0][0]]
        else:
            new_size = n//2
            
            self.a11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
            self.a12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
            self.a21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
            self.a22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

            self.b11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
            self.b12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
            self.b21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
            self.b22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

            
            self.split(a,self.a11,0,0)
            self.split(a,self.a12,0,new_size)
            self.split(a,self.a21,new_size,0)
            self.split(a,self.a22,new_size,new_size)
            self.split(b,self.b11,0,0)
            self.split(b,self.b12,0,new_size)
            self.split(b,self.b21,new_size,0)
            self.split(b,self.b22,new_size,new_size)
            

            M1 = self.multiply(self.add(self.a11, self.a22), self.add(self.b11, self.b22))
            M2 = self.multiply(self.add(self.a21, self.a22), self.b11)
            M3 = self.multiply(self.a11, self.sub(self.b12, self.b22))
            M4 = self.multiply(self.a22, self.sub(self.b21, self.b11))
            M5 = self.multiply(self.add(self.a11, self.a12), self.b22)
            M6 = self.multiply(self.sub(self.a21, self.a11), self.add(self.b11, self.b12))
            M7 = self.multiply(self.sub(self.a12,self.a22), self.add(self.b21, self.b22))
            
            C11 = self.add(self.sub(self.add([M1],[M4]),[M5]),[M7])
            C12 = self.add([M3], [M5])
            C21 = self.add([M2], [M4])
            C22 = self.add(self.sub(self.add([M1], [M3]), [M2]),[ M6])

            
            self.join(C11, self.R, 0 , 0);
            self.join(C12, self.R, 0 , n//2);
            self.join(C21, self.R, n//2, 0);
            self.join(C22, self.R, n//2, n//2);

            return self.R

         
    def split(self,c,p,i,j):
        i2=i;j2=j
        
        for i1 in range(0,len(p)):
            for j1 in range(0,len(p)):
                print(i1,j1,i2,j2)
                p[i1][j1] = c[i2][j2];
                j2+=1
            i2+=1

    def join(self,c,p,i,j):
        i2=i;j2=j
        
        for i1 in range(0,len(c)):
            for j1 in range(0,len(c)):
                p[i2][j2] = c[0][0];
                j2+=1
            i2+=1
    
    def add(self,c,p):
        n=len(p)
        c1=[[0 for j in range(0,n)] for i in range(0,n)]
        for i in range(n):
            for j in range(n):
                c1[i][j]=c[i][j]+p[i][j]
        return c1

    def sub(self,c,p):
        n=len(p)
        c1=[[0 for j in range(0,n)] for i in range(0,n)]
        for i in range(n):
            for j in range(n):
                c1[i][j]=c[i][j]-p[i][j]
        return c1
                
A=Strassen()

