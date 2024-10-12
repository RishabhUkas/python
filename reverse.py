def reverse(N):
    
    rev= N[::-1]
    return rev

T = int(input())
for i in range(0,T):
    N =input()

    print(reverse(N))