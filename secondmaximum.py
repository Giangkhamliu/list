list1=[1,-2,6,8,-1,-7,-6]
i=0
while i<len(list1):
    j=0
    while j<len(list1):
        if list1[i]<list1[j]:
            b=list1[i]
            list1[i]=list1[j]
            list1[j]=b
        j+=1
    i+=1
print(b)
        