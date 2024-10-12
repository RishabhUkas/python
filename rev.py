t= int(input())
for i in range(0,t):
    a=int(input())
    rev=0
    while a>0:
        digit= a%10
        rev = rev*10 + digit
        a=a//10
    print(rev)
