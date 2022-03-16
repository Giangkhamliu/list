s=input("Enter the string:-")
a=""
b=""
i=0
while i<len(s):
        if s[i]!="," and s[i]!=" ":
                a+=s[i]
        i+=1
print("the string is",a)
c=a.upper()
print("the string after the conversion:-",c)
j=-1
while j>(-(len(c)+1)):
        b+=c[j]
        j-=1
if b==c:
        print(c,"True")
else:
        print(c, "False")
