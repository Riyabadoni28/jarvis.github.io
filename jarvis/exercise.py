
print("how many row want to print")
n=int(input())
print("which patten want to print")
p=int(input())
p=int(p)

if p == 0:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
elif p == 1:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
