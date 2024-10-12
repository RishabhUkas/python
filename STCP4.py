a,b = input().split()
a, b = int(a), int(b)
num, tt = 0, "12356890"
for i in range(a,b):
    s = str(i)
    for k in "47":
      if k in s:
        if "0" not in s and "1" not in s and "2" not in s and "3" not in s and "5" not in s and "6" not in s and "8" not in s and "9" not in s :
           num+=1
           break
            
print(num)
