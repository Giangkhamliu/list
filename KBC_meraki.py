question= [
"1.How many continents are there?",
"2.What is the capital of India?",
"3.NG mei kaun se course padhaya jaata hai?"
]

options=[
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution=[3,4,1]
i=0
j=0
while i<len(question)and j<len(options):
    print(question[i])
    k=0
    while k<(len(options)+1):
        print(k+1,options[j][k])
        k+=1
    sol=int(input("Enter the solution:"))
    if sol==solution[i]:
        print("Congratulation!! Your Answer is correct.")
    else:
        print("Better luck next time.")
        break
    print()
    i=i+1
    j+=1
   
    




    
  