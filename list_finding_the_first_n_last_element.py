list=['abc', 'xyz', 'aba', '1221']
i=0
count=0
while i<len(list):
    if list[i][0]==list[i][-1]:
        count+=1
    i+=1
print(count)

# a=["age","aa","axy","123","121","1"]
# i=0
# while i<len(a):
#     if len(a[i])>=3:
#        if a[i][0]==a[i][-1]:
#           print(a[i])
#     i+=1
    