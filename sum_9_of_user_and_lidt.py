a=[1,2,3,4,5,6,7,8]
n=int(input("Enter the number:-"))
i=0
sum=0
c=[]
while i<len(a):
    sum=a[i]+n
    if sum==9:
        c.append(i)
    i+=1
print("The index is:-",c)
    