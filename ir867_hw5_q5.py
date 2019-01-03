#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Homework 5
#Problem 5
s = input("Enter a password: ")
upper=0
lower=0
num=0
special = 0
if len(s)>=8:
    for i in s:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
        if i in "0123456789":
            num+=1
        if i in "!@#$":
            special+=1
if(upper>=2 and lower>=1 and num>=2 and special>=1 and len(s)>=8):
    print(s+" is a valid passowrd.")
else:
    print(s+" is not a valid password.")
