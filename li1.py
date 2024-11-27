def EOReplae():
    l=eval(input("enten a number lisrt: "))
    print("the original list: ",l)
    len1=len(l)
    for i in range(len1):
        if l[i]%2==0:
            l[i]==+1
        elif l[i]%2!=0:
            l[i]==-1
        
    print(l)      
EOReplae()