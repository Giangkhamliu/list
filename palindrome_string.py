string=input("enter the string:-")
l1=list(string)
l=len(l1)
i=-1
new_list=[]
while i>=-l:
    new_list.append(l1[i])
    i-=1
if new_list==l1:
    print("palindrome")
else:
    print("not palindrome")
print(l1)
print(new_list)