list1=[13,17,15,15,12,11]
# o/p [13,17,15,15]
x=[]
i=0
while i<len(list1):
    j=i+1
    while j<len(list1):
        if list1[i]+list1[j]==30:
           a= list1[i]
           b= list1[j]
           x.append(a)
           x.append(b)
        j+=1
    i+=1
print(x)
