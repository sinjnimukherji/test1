def longlines():
    f=open("once upon a time.jpg","r")
    st=f.readLines()
    for i in st:
        line=i.split(' ')
        if len(line)>=10:
            print(i)
    f.close()        