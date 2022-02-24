list1=[1,2,3,4,5,6,7]
a=[]
i=0
j=i+1
while i<len(list1) and j<len(list1):
    new_list= list1[j]-list1[i]
    a.append(new_list)
    j+=1
    i+=1
print(a)
