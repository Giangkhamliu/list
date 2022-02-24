# [[1,2],[3,4],[5,6],[7,8]]
a=[1,2,3,4,5,6,7,8]
i=0
b=[]
while i<len(a)-1:
    s=[]
    s.append(a[i])
    s.append(a[i+1])
    b.append(s)
    i=i+2
print(b)
    
