elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
odd=0
even=0
sum_odd=0
sum_even=0
avg_odd=0
avg_even=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        even+=1
        sum_even+=elements[i]
        avg_even=sum_even/even

    else:
        odd+=1
        sum_odd+=elements[i]
        avg_odd=sum_odd/odd
    i+=1
print("avg of odd=",avg_odd)
print("avg of even=",avg_even)
print("sum of odd=",sum_odd)
print("sum of even=",sum_even)
print("no. of odd=",odd)
print("no. of even=",even)