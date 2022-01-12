a=[34, -345, -1, 100]
largest=a[0]
i=0
while i<len(a):
    if a[i]>largest:
        largest=a[i]
    i+=1
print("The largest is=",largest)