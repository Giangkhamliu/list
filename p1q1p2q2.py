list=['p','q']
lists=[]
n=5
j=1
while j<=n:
    i=0
    while i<len(list):
        new_list=list[i]+str(j)
        lists.append(new_list)
        i+=1
    j+=1
print(lists)
