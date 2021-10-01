def union(cricket, badminton):                            
    L = list(cricket)  
    for i in badminton:
        if i not in cricket:
            L.append(i)
    return L

def intersection(cricket,badminton):
    L = []
    for i in cricket:
        if i in badminton:
            L.append(i) 
    return L

def neither_or(cricket, badminton):
    u = union(cricket, badminton)
    i = intersection(cricket, badminton)
    for value in i:
        u.remove(value)
    return u

def minus(cricket, badminton):
    L = list(cricket)
    for i in badminton:
        if i in L:
            L.remove(i)
    return L

def main():
    cricket= []
    badminton = []
    football = []

    for _ in range(int(input("How many want to play cricket: "))):
        cricket.append(int(input("Enter Roll numbers: ")))
        
    for _ in range(int(input("How many want to play batminton: "))):
        badminton.append(int(input("Enter Roll numbers: ")))

    for _ in range(int(input("How many want to play football: "))):
        football.append(int(input("Enter Roll numbers: ")))

    print(f" Play's both Cricket and Badminton: {intersection(cricket, badminton)} ")
    print(f" Play's Cricket or Badminton but not both: {neither_or(cricket, badminton)} ")
    print(f" Play's neither Cricket nor Badminton: {minus(minus(badminton, cricket), football)} ")
    print(f" Cricket and Football but not Badminton: {minus(intersection(cricket, football), badminton)} ")

main()
 
