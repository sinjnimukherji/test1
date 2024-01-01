# change the first and last letter of each word in the string into upper case 
string = "hello world" 
i= len(string)
S1= string.split()
result=[]
for a in S1:
    result.append(a[0].upper() + a[1:-1] + a[-1].upper())
print(" ".join(result) )