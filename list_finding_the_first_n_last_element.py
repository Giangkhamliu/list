list=['abc', 'xyz', 'aba', '1221']
i=0
count=0
while i<len(list):
    if list[i][0]==list[i][-1]:
        count+=1
    i+=1
print(count)