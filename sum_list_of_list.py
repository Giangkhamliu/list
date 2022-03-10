a=[[16,2],[11,3],[6,1],[2,5]]
#[[18],[14],[7],[7]]
i=0
b=[]
while i<len(a):
    sum=0
    j=0
    c=[]
    while j<len(a[i]):
        sum+=a[i][j]
        j+=1
    c.append(sum)
    b.append(c)
    i+=1
print(b)