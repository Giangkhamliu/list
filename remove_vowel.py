s=input("Enter the string:-")
vowels = ['a','e','i','o','u']
for i in s:
    if i.lower() in vowels:
        print("",end="")
    else:
        print(i,end="")
     