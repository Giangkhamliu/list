name=['n','i','t','i','n']
a=[]
i=-1
while i>=(-len(name)):
    a.append(name[i])
    i-=1
print(a)
print(name)
if name==a:
    print("YES! Palindrome")
else:
    print("NO! Not Palindrome")