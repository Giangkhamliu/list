# 1.Take 10 integer inputs from user and store 
# them in a list and print them on screen.
# i = 10
# a = []
# while i>0:
#   print("Enter number:")
#   num = input()
#   a.append(num)
#   i = i-1
# print(a)

# 2.Take 10 integer inputs from user and store them in a list. 
# Again ask user to give a number. Now, tell user whether that
#  number is present in list or not.
# (Iterate over list using while loop ).
i = 10
a = []
while i>0:
  print("Enter number:")
  num = input()
  a.append(num)
  i = i-1
n=input("ENTER ANY NUMBER")
if n in a:
    print("Yes")
else:
    print("No")