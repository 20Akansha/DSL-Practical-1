                                             #practical 3

m=int(input('enter rows : '))
n=int(input('enter columns :'))

a=[]
b=[]
c=[]

for i in range(m):
    out= []
    for j in range(n):
        num=int(input('enter the numbers :'))
        out.append(num)
    a.append(out)
print(a)


for i in range(m):
    out = []
    for j in range(n):
        num=int(input('enter the numbers :'))
        out.append(num)
    b.append(out)
print(b)


for i in range(m):
    out=[]
    for j in range(n):
      out.append(0)
    c.append(out)


                      #performing operations

def add():
     for i in range (m):
         for j in range(n):
            c[i][j]=a[i][j]+b[i][j]

     for r in c:
        print("The sum is",r)
                
                
def sub():    
     for i in range (m):
         for j in range(n):
            c[i][j]=a[i][j]-b[i][j]
     for r in c:
        print("the diff is",r)
                

def mul():
   
    for i in range(len(a)):  
        for j in range(len(b[0])):  
           for k in range(len(b)):  
               c[i][j] += a[i][k] * b[k][j]
               
    for r in c:  
         print("The Mul is ",r) 

def trans(a):
    
    for i in range(len(a)):  
       for j in range(len(a[0])):  
           c[j][i] = a[i][j]  
    for r in c:  
        print("Transpose of matrix ",r)

def trans(b):
   
    for i in range(len(b)):  
       for j in range(len(b[0])):  
           c[j][i] = b[i][j]  
    for r in c:  
        print("Transpose of matrix ",r)        

add()      
sub()
mul()
trans(a)
trans(b)


