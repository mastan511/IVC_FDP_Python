# 5

# *****
# *   *
# *   *
# *   *
# *****

# 3

# ***
# * *
# ***

def hsst(size):
    for i in range(1,size+1):
        for j in range(1,size+1):
            print(i,end="")
        print(end="\n")
    return

def hasq(s):
    for i in range(1,s+1):
        for j in range(1,s+1):
            if i==1 or j==1 or i==s or j==s:
                print("*",end="")
            else:
                print(" ",end="")
        print(end="\n")
    return

def crsd(k):
    for i in range(1,k+1):
        for j in range(1,k+1):
            if i==j or i+j==k+1:
                print("*",end="")
            else:
                print(" ",end="")
        print(end="\n")
    return








