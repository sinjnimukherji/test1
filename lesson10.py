islist=[]
s=int(input("enter how many elements u want to enter : "))
print ("enter", s,"numbers")
for n in range(s):
    l1=int(input(":- "))
    islist.append(l1)
print(" the alternate list are :' ")
for i in range (0,s,2):
    print(islist[i])    