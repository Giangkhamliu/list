list1=[5,8,9,23,6]
max=0
i=0
while i<len(list1):
    if list1[i]>max:
        max=list1[i]
    i=i+1
print(max)