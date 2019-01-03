#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Homework 5
#Problem 4

s = input("Enter a string: ")
new = ""
new +=s[0].upper()
i=1
while i<len(s):
    if(s[i]==" "):
        new+=s[i]+s[i+1].upper()
        i+=2
    elif s[i] in ".,;?!" and i!=len(s)-1:
        new+=s[i]+s[i+1].upper()
        i+=2
    else:
        new+=s[i]
        i+=1
print(new)
