# ["NavGurukul","is","residential","page"]
a="NavGurukul is residential page"
i=0
b=[]
s=""
while i<len(a):
    if a[i]==" ":
        b.append(s)
        s=""
    else:
        s+=a[i]
    i+=1
b.append(s)
print(b)