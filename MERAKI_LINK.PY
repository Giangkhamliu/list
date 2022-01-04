list=["Python","Java","c","C","C++"]
print(max(list))

list=["mary","tom","simon"]
list.insert(8,5)
print(list)

L=list("www.csiplearninghub.com")
print(L[20:-1])

L=[1,2,3,4,5]
for i in L:
    print(i,end=" ")
    i+=1

#OUTPUT
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 4, 6, 8, 10]
# [5, 10]
# [6]
num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=0
while n<len(num):
    n+=1
print(num[n])