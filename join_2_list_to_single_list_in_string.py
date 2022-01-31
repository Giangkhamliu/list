a=[["Grace"],["pamei"]]
b=[]
i=0            
while i<len(a):
    j=0
    d=[]
    while j<len(a[i]):
        b.append(a[i][j])
        c="".join(b)
        j+=1
    d.append(c)
    i+=1
print(d)