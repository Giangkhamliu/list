##[7, 8, 3, 1, 6, 2, 3, 0, 5]
a=[4,2,7,10,5,9,7,20,6]
b=[]
i=0
while i<len(a):
        j=0
        c=0
        while j<len(a):
                if a[j]>a[i]:
                        c+=1
                j+=1
        b.append(c)
        i+=1
print(b)    