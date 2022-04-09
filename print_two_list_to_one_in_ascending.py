list1=[1,5,2,7,5,9]
list2=[7,4,54,1,3]
list1.extend(list2)
l=[]
for i in list1:
      if i  not in l:
            l.append(i)
print(sorted(l))