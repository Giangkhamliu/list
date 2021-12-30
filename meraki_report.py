marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
mark1=marks[0]
mark2=marks[1]
mark3=marks[2]
sum=0
sum1=0
sum2=0
i=0
j=0
k=0
while i<len(mark1):
     sum=sum+mark1[i]
     i+=1
while j<len(mark2):
     sum1=sum1+mark2[j]
     j+=1
while k<len(mark3):
     sum2=sum2+mark3[k]
     k+=1
print(sum+sum1+sum2)
