# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(len(numbers))

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
count=0
i=0
# while i<len(numbers):
for i in range(len(numbers)):
    if numbers[i]>=20 and numbers[i]<=40:
       count=count+1
       print(count)
    i=i+1
    
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i+=1
print("The maximum no. is=",max)

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
numbers.sort()
print("The maximum no. is=",numbers[-2])

places=["delhi", "gujarat", "rajasthan", "punjab", "kerala"]
i=1
while i<len(places)+1:
    print(places[-i])
    i=i+1


#PALINDROME
name=['n','i','t','i','n']
name=['g','r','a','c','e']
rev=reversed(name)
if list(name)==list(rev):
    print("palindrome")
else:
    print("NOt palindrome")




