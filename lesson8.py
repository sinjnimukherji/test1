#user input name to print the its initials.
text= input("enetr yttour name : ")
count1= text.find(' ')
count2= text.find(' ',count1+1)
txt=text[0]+'.'+text[count1+1]+'.'+text[count2+1]
print("the result: ",txt)