list1=[1,2,3,4]
str1="emp"
list=[]
i=0                                                                                                  
while i<len(list1):
    new_list=str1+str(list1[i])
    list.append(new_list)
    i+=1
print(list)