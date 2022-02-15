# a=[1,2,3,4,5,6,]
# i=2
# b=[]
# while i<=len(a):
#     j=2
#     sum=0
#     while j<i:
#         if i%j==0:
#             sum+=1
#         j+=1
#     if sum==0:
#         b.append(i)
    
#     i=i+1
# print(b)


# list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# str=" "
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         str=str+list[i][j]
#         j=j+1
#     i=i+1
# print(str)

# a=['1', '2', '3', '4', '5', '6', '7', '8']
# i=0
# b=[]
# while i<len(a)-1:
#     b.append((a[i])+(a[i+1]))
#     i=i+2
# print(b)


# list1=[1,1,2,3,4,5,1,2]
# a=int(input("enter the number:-"))
# i=0
# while i<len(list1):
#     if a in list1:
#       list1.remove(a)
#     i=i+1 
# print(list1)



# list1 = [2, -7, 5, -64, -14]
# i=0
# nag=0
# post=0
# while i<len(list1):
#     if list1[i]>=0:
#         post+=1
#     else:
#         nag+=1
#     i=i+1
# print("post",post)
# print("nag",nag)

# Output: pos = 2, neg = 3

a="my name is Grace"
b=[]
b=a
i=0
while i<len(b):
    if b[i] in b[2]:
        print("-",end="")
    else:
        print(b[i],end="")
    i+=1

list1=["m","na","i","gra"]
list2=["y","me","s","ce"]
i=0
c=[]
while i<len(list1):
    d=(list1[i]+list2[i])
    c.append(d)
    i=i+1
print(c)

# list=input("Enter the number:")
# i=0
# while i <len(list):
#     reverse=list[-2:0:-1]
#     i+=1
# print(reverse)


a="my name is Grace"
i=0
s=""
while i<len(a):
    if a[i]==" ":
        c=a[i].replace(" ","-")
        s=s+c
    else:
        s=s+a[i]
    i=i+1
print(s)