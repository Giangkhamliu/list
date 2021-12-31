marks = [
[78, 76, 94, 86, 88],
[91, 71, 98, 65],
[95, 45, 78]
]

for i in range(len(marks)):
   sum=0 
   avg=0
   for j in range(len(marks[i])):
      sum=sum+marks[i][j]
      avg=sum/len(marks[i])
   print("Average of",i, "year=",int(avg))
##while loop
marks = [[78, 76, 94, 86, 88],
[91, 71, 98, 65],
[95, 45, 78],
[87, 67, 49, 68, 88]]
i=0
while i<len(marks):
   j=0
   sum=0 
   avg=0
   while j<len(marks[i]):
      sum=sum+marks[i][j]
      avg=sum/len(marks[i])
      j+=1
   i+=1
   print("Average of",i, "year=",avg)