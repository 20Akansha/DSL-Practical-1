n=int(input("Enter the total number of students : "))                                        #practical 1
s=[]
for i in range(n):
    marks=int(input(f"enter marks of {i+1} :"))
    s.append(marks)
print("the list of marks of student is ",s)


def average(num):
    sum = 0
    total=0
    for i in num:
        sum +=i
        total+=1

    avg = sum / total
    return avg
avg=average(s)
print("the average of students is",avg)


def max():
      
         max_value = None
         if i !=-999:
              for num in s:
                 if (max_value is None or num > max_value):
                    max_value = num
         print('The max marks is:', max_value)

         
def min():
      
         mini = s[0]
         for i in range(len(s)):
                if s[i] < mini:
                    mini = s[i] 
         print("The least marks is ",mini)


def frequency():
        max = 0
        res = s[0]
        total=0
    
        for i in s:
            for j in range(1,len(s)):
                if (s[j] == s[j - 1]):
                    total+=1
                    if total> max:
                        max = total
                        res = s[j-1]
            return res
print("The most frequent marks is",frequency())            


def absent():
            
            ab=0
            for i in s:
                if i ==-999:
                     ab+=1
                else:
                    pass
                    
            print("The number of absent students are",ab)
     
            
max()
min()
absent()
