x=1
y=2
z=x+y

def Calculate(A,B,C):
    if A==True:
        return B+C
    else:
        return B-C

def readFile(filename):
    f=open(filename)
    data=f.read()
    return data

l = [1,2,3,4,5]
for i in range(0, len(l)):
    print(l[i])