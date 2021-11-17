#searching methods

n=int(input("Enter roll numbers:"))
s=[]
for i in range(n):
    std=int(input("Enter roll num:"))
    s.append(std)


def linearsearch(a,k):
      for i in range(n):
            if a[i]== k:
                  return i
key1=int(input("Enter the element to be found: "))
L=linearsearch(s,key1)
print("The element found at index",L)  

   
def sentinelsearch(b,k):
    b.append(k)
    i= 0 
    while True:
        if b[i] == k: 
            break
        i+=1
    return i
key2=int(input("Enter the element to be found: "))
S=sentinelsearch(s,key2)
print("The element found at index",S)


def binarysearch(c, k):
    low = 0
    high = len(c)- 1
    mid = 0 
    while low <= high:
        mid = (high + low)// 2
        if c[mid]<k:
            low = mid + 1
        elif c[mid] > k:
            high = mid - 1
        else:
            return mid
    
key3=int(input("Enter the element to be found:"))
binary=binarysearch(s,key3)
print("the element is found at",binary)


def fibsearch(arr,key):
    b=0
    a=1
    f=b+a
    while(f<n):
        b=a
        a=f
        f=b+a
    offset=-1
    while(f>1):
        i=min(offset+b,n-1)
        if(arr[i]<key):
            f=a
            a=b
            b=f-a
            offset=i
        elif(arr[i]>key):
            f=b
            a=a-b
            b=f-a
        else:
            return i
        if(a and arr[offset+1]==key):
            return offset+1
    
        
keyfib=int(input("Enter the element to be found using fib search"))
fib=fibsearch(s,keyfib)
print("the element is found at",fib)
































