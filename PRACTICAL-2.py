def union(c,b):
  l=list(c)
  for i in  b  :
    if i not in c  :
      l.append(i)
  return l

def intersection(c,b):
  l=[]
  for i in c:
    if i in b:
      l.append(i)
  return l 

def either(c,b):
  u=union(c,b)
  i=intersection(c,b)
  for value in u:
    if value in i:
      u.remove(value)
  return u   

def neither(c,b,team):
  l=[]
  for i in team:
    if i not in c:
        if i not in b:
            l.append(i)
  return l

def inter(c,f,b):
    l=[]
    for i in c:
        if i in f:
            if i not in b:
                l.append(i)
    return l            

def cls():
  team=[]
  c=[]
  b=[]
  f=[]

  for _ in range(int(input("Enter total std in class:"))):
    team.append(int(input("Enter std: ")))
  for _ in range(int(input("Enter std playing criket:"))):
    c.append(int(input("Enter std: ")))
  for _ in range(int(input("Enter std playing badminton:"))):
    b.append(int(input("Enter std: ")))
  for _ in range(int(input("Enter std playing football:"))):
    f.append(int(input("Enter std: ")))

  print(f"The std who plays both c n b:{intersection(c,b)}")
  print(f"The std who plays either c n b but not both:{either(c,b)}")
  print(f"The std who plays neither c or b :{neither(c,b,team)}")
  print(f"The std who plays both c n f but not b :{inter(c,f,b)}")
  
  
cls()
