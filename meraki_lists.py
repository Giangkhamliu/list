# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(len(numbers))

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
count=0
i=0
# while i<len(numbers):
for i in range(len(numbers)):
    if numbers[i]>=20 and numbers[i]<=40:
       count=count+numbers[i]
       print(numbers[i])
    i=i+1
    
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# max(numbers)
# print(max(numbers))
numbers.sort()
print(numbers)
print("The maximum no. is=",numbers[-1])

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
numbers.sort()
print("The maximum no. is=",numbers[-2])

places=["delhi", "gujarat", "rajasthan", "punjab", "kerala"]
# print(places[4])
# print(places[3])
# print(places[2])
# print(places[1])
# print(places[0])
i=1
while i<len(places)+1:
    print(places[-i])
    i=i+1

# name=[ 'n', 'i', 't', 'i', 'n' ]
name=['g','r','a','c','e']
if name[0]==name[4]:
    print(name,"Palindrome")
else:
    print(name,"Not palindrome")
    




    