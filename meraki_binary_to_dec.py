# bin_num=[1,0,0,1,1,0,1,1]
# string=[str(bin) for bin in bin_num]
# a_string="".join(string)
# an_bin=int(a_string)
# decNum=0
# power=0
# while an_bin>0:
#     decNum=decNum+2**power*(an_bin%10)
#     an_bin=an_bin//10
#     power+=1
# print("Decimal=",decNum)

# binary_number = [1,0,0,1,1,0,1,1]
# strings=[str(binary)for binary in binary_number]
# a_string="".join(strings)
# dec=int(a_string)
# decimal=0
# power=0
# while dec>0:
#     decimal+=2**power*(dec%10)
#     dec//=10
#     power+=1
# print ("Decimal :-",decimal)

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
     
