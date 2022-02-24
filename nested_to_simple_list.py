# list=["a","b",["c",["d","e"],["j","g"],"k"],"l","m","n"]
# list1=[lists for sublist in list for lists in sublist]
# list2=[list for sublist in list1 for list in sublist]
# print(list2)

# list=["a",'b',['c',['d','e'],['j','g'],'k'],'l','m','n']
# flat_list = []
# for sublist in list:
#     for num in sublist:
#         for sublist in num:
#             for num in sublist:
#                 flat_list.append(num)

# print(flat_list)

# list=["a",'b',['c',['d','e'],['j','g'],'k'],'l','m','n']
# i=0
# c=[]
# e=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         b=list[i][j]
#         c.append(b)
#         j+=1
#     i+=1
# print(c)
# k=0
# while k<len(c):
#     l=0
#     while l<len(c[k]):
#         d=c[k][l]
#         e.append(d)
#         l+=1
#     k+=1
# print(e)

list=[0,1,2,[3,4],5,6,7,[8]]
print(str(list[0])+str(list[3][1])+str(list[4])+str(list[7][0]))       