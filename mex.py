'''D=int(input())
if D%7==0:
    print("YES")
else:
    print("NO")'''

N,M = map(int,input().split())

A= list(map(int,input().split()))

B= list(map(int,input().split()))

for i in range(N):
    for j in range(i):

        if(B[j]<0):
            A[i]=A[i-B[j]]
        if(B[j]>0):
            A[i]=A[i+B[j]]
        
for i in range(N):
    print(A[i],sep=" ")