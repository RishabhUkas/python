roman= {
"I":            1,
"V":            5,
"X" :            10,
"L" :            50,
"C" :            100,
"D"  :           500,
"M"  :          1000}


s="III"
sum=0
for i in range( 0, len(s)-1):

    if roman[s[i]]<roman[s[i+1]]:
        sum-=roman[s[i]]

    else:
        sum+=roman[s[i]]

sum+= roman[s[-1]]

print(sum)