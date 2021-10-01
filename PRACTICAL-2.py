def union(criket, badminton):                            
    L = list(criket)  
    for i in badminton:
        if i not in criket:
            L.append(i)
    return L

def intersection(criket,badminton):
    L = []
    for i in criket:
        if i in badminton:
            L.append(i) 
    return L

def eiter_or(criket, badminton):
    u = union(criket, badminton)
    i = intersect(criket, badminton)
    for value in i:
        u.remove(value)
    return u

def minus(criket, badminton):
    L = list(criket)
    for i in badminton:
        if i in L:
            L.remove(i)
    return L

def main():
    criket= []
    badminton = []
    football = []

    for _ in range(int(input("How many want to play cricket: "))):
        criket.append(int(input("Enter Roll numbers: ")))
        
    for _ in range(int(input("How many want to play batminton: "))):
        badminton.append(int(input("Enter Roll numbers: ")))

    for _ in range(int(input("How many want to play football: "))):
        football.append(int(input("Enter Roll numbers: ")))

    print(f"Play's both Cricket and Badminton:{union(criket, badminton)} ")
    print(f"Play's Cricket or Batminton but not both:{eiter_or(criket, badminton)} ")
    print(f"Play's neitner Cricket nor Football:{minus(minus(badminton, criket), football)} ")
    print(f"Play's Cricket and Football but not Batminton:{minus(intersect(criket, football), badminton)} ")

main()
 
