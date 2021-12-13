# number=[2,4,5,6,7]
# i=0
# while i<len(number):
#     print(number[i])
#     i=i+1
i=5
a=[]
while i>0:
  print("Enter the number:")
  num=input()
  a.append(num)
  i-=1
odd=0
even=0
positive=0
negative=0
zero=0
i=19
while i>=0:
  if a[i]==0:
    zero=zero+1
  elif a[i]>0:
    positive=positive+1
    if a[i]%2==0:
      even=even+1
    else:
      odd=odd+1
  else:
    negative=negative+1
    if a[i]%2==0:
      even=even+1
    else:
          odd=odd+1
  i-=1
print("EVEN:",even,"ODD:",even,"POSITIVE:",positive,"NEGATIVE:",negative,"ZERO",zero)