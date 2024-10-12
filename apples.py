'''X,Y =(input().split())

A=int(X)
B= int(Y)

sum=A+B

if(sum%2==0):
    print("YES")
else:
    print("NO")'''



'''T=int(input())
for i in range(0,T):
    N= int(input())
    if((N +1 )%3==0 or (N-1)%3==0):
        print("YES")
    else:
        print("NO")'''


'''import math

total_words , max_words = input().split()

w=int(total_words)
k=int(max_words)

div = w/k

x= math.ceil(div)
y= math.floor(div)

print(f"{x} {y}")'''

'''T=int(input())
for i in range(0,T):
    A ,B =input().split()
    a = int(A)
    b = int(B)
   

    for j in range(1,min(a,b)+1):
        if(a%j==0 and b%j==0):
            p = a//j
            q = b//j
    print(f"{p} {q}") '''

'''T=int(input())
for i in range(0,T):
      a,b,c,k=map(int,input().split())
      
      max_apple = max(a,b,c)
      if(a==b==c==k):
            print("YES")
      elif((max_apple-a)%k==0 and (max_apple-b)%k==0 and (max_apple-c)%k==0 ):
            print("YES")
      else:
            print("NO")'''


