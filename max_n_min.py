a=[]
i=0
while i<10:
        user=int(input("Enter the number:-"))
        a.append(user)
        i+=1
print(a)
small=a[0]
j=0
while j<len(a):
        if a[j]<small:
                small=a[j]
        j+=1
big=0
k=0
while k<len(a):
        if a[k]>big:
                big=a[k]
        k+=1
print("The biggest",big)
print("The smallest",small)