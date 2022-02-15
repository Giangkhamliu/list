# Write a Python program to convert a given list of strings into list of lists.
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'],
#  ['O', 'l', 'i', 'v', 'e']]
a=['Red', 'Maroon', 'Yellow', 'Olive']
b=[]
i=0
while i<len(a):
    c=[]
    j=0
    while j<len(a[i]):
        c.append(a[i][j])
        j+=1
    b.append(c)
    i+=1
print(b)