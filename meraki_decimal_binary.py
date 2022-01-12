decNum= [155]
strings = [str(dec) for dec in decNum]
an_bin = "". join(strings)
a_string = int(an_bin)
binNum=0
power=0
while a_string>0:
    binNum+=10**power*(a_string%2)
    a_string//=2
    power+=1
print("The Binary no. =",binNum)
