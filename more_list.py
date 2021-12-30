# Make a list by taking 10 input from user. 
# Now delete all repeated elements of the list.
a = [1,2,3,2,1,3,12,1,12,3,32]
i = 0
while i < len(a):
  j = i+1
  while j < len(a):
    if a[i] == a[j]:
      del(a[j])
    j=j+1
  i = i+1
print (a)


# Ask user to give integer inputs to make a list.
#  Store only even values given and print the list.
n=int(input("Enter the numbers:"))
a=[]
i=0
while i<n:
   num=int(input("Enter the number:"))
   if num%2==0:
      a.append(num)
   i+=1
print(a)
# Take a list of 10 elements. Split it into middle and store 
# the elements in two dfferent lists. E.g.-
# INITIAL list :
# 58	24	13	15	63	9	8	81	1	78

a=[58,24,13,15,63,9,8,81,1,78]
i=0
j=len(a)/2
while i<j:
  i+=1
print(a[:i])
print(a[i:])
