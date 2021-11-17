
list= []                                           #bubble sort

num = int(input("Enter total number of elements : "))
for i in range(num):
    value = int(input(f"Enter the elements {i+1}: "))
    list.append(value)

for i in range(num -1):
    for j in range(num - i - 1):
        if(list[j] > list[j + 1]):
             c = list[j]
             list[j] = list[j + 1]
             list[j + 1] = c
print("Sorted List: ", list)

                                                    #insertion sort

def insertion_sort(sort):
    for i in range(1, len(sort)):
        A= sort[i]
        j = i - 1
        while j >= 0 and A < sort[j]:
            sort[j + 1] = sort[j]
            j -= 1
        sort[j + 1] = A
    print("The sorted list:", sort)
   
l= []
length= int(input("Enter number of elements in list: "))
for i in range(length):
    elements = int(input("Enter the element: "))
    l.append(elements)
insertion_sort(l)



def partition(arr,left,right):              #Quick sort
  i=left+1
  pivot=arr[left]
  for j in range(left+1,right+1):
    if arr[j]<pivot:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
  pos=i-1
  arr[left],arr[pos]=arr[pos],arr[left]
  return pos

n=int(input("Enter total number of elements: "))
print("Enter elements: ")

  
def Quick_sort(arr,left,right):
  if left<right:
    pivot=partition(arr,left,right)
    Quick_sort(arr,left,pivot-1)
    Quick_sort(arr,pivot+1,right)
    
arr={}
for i in range(0,n):
  arr[i]=int(input())
Quick_sort(arr,0,n-1)
print("Sorted array: ")
for i in range(n):
  print(arr[i])


def Merge(std):                                #Merge sort
    if len(std) >1 :
    
        mid = len(std)//2
        left= std[:mid]
        right= std[mid:]
        Merge(left) 
        Merge(right) 
        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if left[i]< right[j]:
                std[k] = left[i]
                i+=1
                k+=1
            else:
                std[k] = right[j]
                j+=1
                k+=1
        while i < len(left):   
            std[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            std[k] = right[j]
            j+=1
            k+=1

n = int(input("Enter no. of elements: "))
std= [int(input()) for i in range(n)]
Merge(std)
print("sorted list : " + str(std))



def SelectionSort(arr):                             #selection sort
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
SelectionSort(list)
print("sorted numbers are: ",list) 


def shellsort(arr,num):                             #shellsort
    gap=num//2
    while gap>0:
        for i in range(gap,num):
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap=gap//2
shellsort(list,len(list))
print("sorted numbers are: ",list)












































































