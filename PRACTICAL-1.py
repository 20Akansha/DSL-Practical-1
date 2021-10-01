n=int(input("Enter the total number of students in class: "))                             #practical 1
FDS=[]
for i in range(n):
    marks=int(input(f"Enter marks of student {i+1} : "))
    FDS.append(marks)
print("The list of marks of students is ",FDS)


def average(num):
    sum=0
    total=0
    for i in num:
        sum+=i
        total+=1
    avg=sum/total
    return avg

avg=average(FDS)
print("The average of marks is:",avg)


def maximum():
    max_value=None
    if i!=-1:
        for num in FDS:
            if max_value is None or num>max_value:
                max_value=num
        print("The maximum marks are: ",max_value)
maximum()        
        

def minimum():
    min_value=None
    for num in FDS:
        num!=-1
        if min_value is None or num<min_value:
            if num>-1:
                min_value=num
    print("The minimum marks are:",min_value)
    
minimum()            


def frequency():
    max=0
    list=FDS[0]
    total=0
    for i in FDS:       
        for j in range(1,len(FDS)):
            if FDS[j]==FDS[j-1]:
                total+=1
                if total>max:
                    max=total
                    list=FDS[j-1]
        return list
    
print("The most frequently occuring marks are",frequency())

              
                    
def absent():
    AB=0
    for i in FDS:
        if i == -1:
            AB+=1
        else:
            pass
    print("The number of absent students is : ",AB)

    
absent()        
 
