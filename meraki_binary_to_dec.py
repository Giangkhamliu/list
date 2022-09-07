a=[]
length=int(input("enter the length:-"))
i=0
while i<length:
    num=int(input("Enter the number:-"))
    a.append(num)
    i+=1
print(a)
i=-1
pow=0
sum=0
while i>=(-len(a)):
    n=a[i]*2**pow
    sum+=n
    pow+=1
    i-=1
print("The Decimal value is=",sum)
     
