# a=['1', '2', '3', '4', '5', '6', '7', '8']
# i=0
# b=[]
# while i<len(a)-1:
#     b.append((a[i])+(a[i+1]))
#     i=i+2
# print(b)


list1=[1,1,2,3,4,5,1,2]
a=int(input("enter the number:-"))
i=0
while i<len(list1):
    if a in list1:
      list1.remove(a)
    i=i+1 
print(list1)



