ms= [[8, 3, 4],
[1, 5, 9],
[6, 7, 2]]
i=0
while i<len(ms):
    row=0
    col=0
    j=0
    while j<len(ms):
        row=row+ms[i][j]
        col=col+ms[j][i]
        j+=1
    i+=1
    print("Row=",row)
    print("Col=",col)
print()
c=0
d=0
f=(len(ms)-1)
d1=0
d2=0
while c<len(ms):
    d1=d1+ms[c][d]
    d2=d2+ms[c][f]
    c+=1
    d+=1
    f-=1
print("diagonal=",d1)
print("diagonal=",d2)
if col==row and d1==d2:
    print("Magic Square")
else:
    print("Not a magic square")