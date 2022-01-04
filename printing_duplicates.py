l=[1, 2, 3, 3, 4, 5, 5, 6, 7]
i=0
c=[]
while i<len(l):
    j=i+1
    while j<len(l):
        if l[i]==l[j]:
            c.append(l[i])
        j=j+1
    i=i+1
print(l)