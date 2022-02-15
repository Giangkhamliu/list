# a=[1,3,4,7]
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
i=0
while i<len(a):
    j=1
    count=0
    while j<=a[i]:
        if a[i]%j==0:
            count+=1
        j+=1
    if count==2:
        print(a[i],"It is a prime no.")
    # else:
    #     print(a[i],"It is not a prime no.")
    i+=1