input_str=input("enter a word: ")
vowels='AEIOUaeiou'
count=0
for i in input_str:
    if i in vowels:
        count=count+1
print(count)