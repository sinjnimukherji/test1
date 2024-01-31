#palindrome string or not
n=input("enter a string: ")
i=len(n) 
k=(n[::-1])
if (n==k):
    print(k,"is a palindrome string")
else :
    print ("not a palindrome string")
