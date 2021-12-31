ms= [
[8, 3, 4],
[1, 5, 9],
[6, 7, 2]
]
i=0
row1=0
row2=0
row3=0
while i<len(ms):
    row1=row1+ms[i][0]
    row2=row2+ms[i][1]
    row3=row3+ms[i][2]
    i+=1
print("Row1=",row1)
print("Row2=",row2)
print("Row3=",row3)
if row1==row2==row3:
    print("yes,it is magic square")
else:
    print("No,it is not magic square")


ms=[
[5, 3, 7],
[1, 8, 9],
[6, 4, 2]
]
i=0
row1=0
row2=0
row3=0
while i<len(ms):
    row1=row1+ms[i][1]
    row2=row2+ms[i][2]
    row3=row3+ms[i][0]
    i+=1
print("Row1=",row1)
print("Row2=",row2)
print("Row3=",row3)
if row1==row2==row3:
    print("yes,it is magic square")
else:
    print("No,it is not magic square")
