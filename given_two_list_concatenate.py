list1=["m","na","i","Gra"]
list2=["y","me","s","ce"]
i=0
j=0
list3=[]
while i<len(list1) and j<len(list2):
    list3.append(list1[i]+list2[j])
    i+=1
    j+=1
print(list3)
