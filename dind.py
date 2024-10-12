
N,Q = map(int,input().split())

l=list(map(int,(input().split())))

list = l[:N]
for i in range(Q):
    Q=int(input())
    if Q in list:
        print("YES")
    else:
        print("NO")



