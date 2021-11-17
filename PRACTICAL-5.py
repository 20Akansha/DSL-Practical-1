def longword():
      S=[]
      n=int(input("How many names are there in the list?"))
      for word in range(0,n):
            name=input("Enter the names:")
            S.append(name)

      max_len=len(S[0])
      l=S[0]
      for word in S:
            if (len(word)>max_len):
                  max_len=len(word)
                  l=word
      print("The name with max length is:",l)
      print("Name length=",max_len)
longword()


def frequency():
      S=input("Enter the String: ")
      dic={}
      for i in S:
            keys=dic.keys()
            if i in keys:
                  dic[i]+=1
            else:
                  dic[i]=1
      print(dic)            
frequency()



def Palindrome():
      S=input("Enter the String:")
      if S==S[::-1]:
            print("The given string is Palindrome")
      else:
            print("The given string is not Palindrome")
Palindrome()            


def Indx():
      S=input("Enter something:")
      word=input("Enter indx to search:")
      for i in range(len(S)-len(word)+1):
            if S[i:i+len(word)]==word:
                  print("Found")
Indx()


def occurance():
      S=input("Enter something:")
      counts=dict()
      names=S.split()
      for name in names:
            if name in counts:
                  counts[name]+=1
            else:
                  counts[name]=1
      print(counts)            
occurance()
































