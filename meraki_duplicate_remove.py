n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
print ("The original list is : ",n)
n1= []
for i in n:
    if i not in n1:
        n1.append(i)
print ("The list after removing duplicates : ",n1)

