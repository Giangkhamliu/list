list=[34,15,88,2]
i=0
smallest=list[0]
while i<len(list):
    if list[i]<smallest:
        smallest=list[i]
    i+=1
print("The smallest is=",smallest)