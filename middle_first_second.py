user1=input("Enter the first name:-")
user2=input("Enter the middle name:-")
user3=input("Enter the last name:-")
a=""
i=0
while i<len(user1) and i<len(user2):
    if user1[i]==user1[0] and user2[i]==user2[0]:
        cap=user1[i].upper()
        cap1=user2[i].upper()
        a=cap+"."+cap1
    i+=1
print(a+"."+user3)