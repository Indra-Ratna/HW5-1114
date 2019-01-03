#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Homework 5
#Problem 3

s = input("Enter a string: ")
acc=0
for i in s:
    if i in ".,;:?!":
        acc+=1
if(acc>0):
    print("This contains punctuation")
else:
    print("This does no contain punctuation")
