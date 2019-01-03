#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Homework 5
#Problem 2
s = input("Enter a string: ")
acc=""
for i in range (0,len(s)):
    if s[i]==" ":
        acc+="_"
    else:
        acc+=s[i]
print(acc)
