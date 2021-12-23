# Write a Python program to compute the difference between two lists. Go to the editor
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
# color1=["red", "orange", "green", "blue", "white"]
# color2=["black", "yellow", "green", "blue"]
# i=0
# j=0
# while i<len(color1) and j<len(color2):
#     color3=list(color1)-list(color2)
#     print("color1-color2:",color3)



# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
# z = zip(name, animal, age)
# for name,animal,age in z:
#     print("%s the %s is %s"%(name, animal, age))

b = [1,2,3]
# b.extend([5,6])
# print(b)
b.append([5,6])
print(b)