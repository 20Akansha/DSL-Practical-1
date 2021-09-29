
                                                             #practical2

criket=[]                                   #initializing empty lists
badminton=[]
football=[]

c = int(input("Enter number of students who play's cricket:  "))
b = int(input("Enter number of students who play's badminton:  "))
f = int(input("Enter number of students who play's football:  "))

for i in range (c):
    criket.append(int(input(f"Enter the roll nos of student {i+1} who play's cricket:  ")))
for i in range (b):
    badminton.append(int(input(f"Enter the roll nos of student {i+1} who play's badminton:  ")))
for i in range (f):
    football.append(int(input(f"Enter the roll nos of student {i+1} who play's football:  ")))

    m=criket.count(i)
    if m>1:
        criket.remove(i)
for i in badminton:
    m=badminton.count(i)
    if m>1:
        badminton.remove(i)
for i in football:
    m=football.count(i)
    if m>1:
        football.remove(i)

    
criket.sort()
badminton.sort()
football.sort()
 
print("The list of students who play's cricket:", criket)
print("The list of students who play's badminton:", badminton)
print("The list of students who play's football:", football )


CB=[]
for i in criket:
    for j in badminton:
        if i==j:
            CB.append(i)
            
print(f"List of students who play both cricket and badmintion are: {CB}")


cb=[]
for i in criket:
    cb.append(i)
    
for i in badminton:
    for j in cb:
        if i!=j:
            cb.append(i)
            break
            
for i in cb:
    p = cb.count(i)
    if p>1:
        cb.remove(i)
        
cb.sort()
print(f"List of students who play either cricket or badminton but not both:{cb}")

ncb = []
for i in football:
    ncb.append(i)
    
list=[]
for k in football:
    for a in cb:
        if a==k:
            list.append(a)           
for b in list:
    ncb.remove(b)
    
count=0
t=0
for i in ncb:
    if t==0:
        count+=1
print(f"Number of students who play neither cricket nor badminton are:{count}")


cfnb=[]
for i in criket:
    for j in football:
        if i==j:
            cfnb.append(i)

for m in cfnb:
    for n in badminton:
        if m==n:
            cfnb.remove(m)
            
count1=0
for d in cfnb:
    if 1>0:
        count1+=1       
print(f"Number of students who play cricket and football but not badminton are:{count1}")

