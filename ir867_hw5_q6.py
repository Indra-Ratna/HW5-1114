#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Homework 5
#Problem 6
n = input("Enter a mathematical expression: ")
operand1 = n[0: n.find(" ")]
operand2 = n[n.rfind(" ")+1:len(n)]

if n[n.find(" ")+1]=="+":
    final = int(operand1)+int(operand2)
    print(str(operand1)+" + "+str(operand2)+" = "+str(final))
elif n[n.find(" ")+1]=="-":
    final = int(operand1)-int(operand2)
    print(str(operand1)+" - "+str(operand2)+" = "+str(final))
elif n[n.find(" ")+1]=="*":
    final = int(operand1)*int(operand2)
    print(str(operand1)+" * "+str(operand2)+" = "+str(final))
