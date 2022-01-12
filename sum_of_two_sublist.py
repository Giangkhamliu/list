list=[1,2,3,4,5]
l1=[]
i=0
j=i+1
while i<len(list)and j<len(list):
    c=list[i]+list[j]
    l1.append(c)
    j+=1
    i+=1
print(l1)

