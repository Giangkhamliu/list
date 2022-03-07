a=[1,2,3,4,'5',6,'7',8]
sum_str=0
sum_int=0
i=0
while i<len(a):
    if a[i]=='5'or a[i]=='7':
        sum_str+=int(a[i])
    else:
        sum_int+=a[i]
    i+=1
print("The sum of string:-",sum_str)
print("The sum of integer:-",sum_int)