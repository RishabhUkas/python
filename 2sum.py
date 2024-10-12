import math
T=int(input())
for i in range(T):
    n=int(input())
    s=input()[:n]
    count_0 =0
    count_1 =0
    for k in range(n):
        if '0'==s[k]:
            count_0+=1
        if '1'==s[k]:
            count_1+=1
    diff=int(math.fabs(count_0-count_1))
    print(diff)