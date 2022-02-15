# # Create a program that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
# # Example: (Input1, Input2 -->Output)

# # "4",  "5" --> "9"
# # "34", "5" --> "39"
# # "", "" --> "0"
# # "2", "" --> "2"
# # "-5", "3" --> "-2"
a=input("Enter the first no.")
b=input("Enter the second no.")
if a=="" and b=="":
    print("0")
elif a=="":
    print(b)
elif b=="":
    print(a)
elif a!="" and b!="":
    print(str(int(a)+int(b)))



# # Create a program that checks if a number n is divisible by two numbers x AND y.
# #  All inputs are positive, non-zero digits.
# # Examples:
# # 1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
# # 2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
# # 3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
# # 4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5

#  n=int(input("Enter any numbers."))
# x=int(input("Enter the first numbers."))
# y=int(input("Enter the second numbers."))
# if n%x==0 and n%y==0:
#     print(True)
# else:
#     print(False)

