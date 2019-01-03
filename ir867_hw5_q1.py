#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Homework 5
#Problem 1
"""
mystery 1 will print every other letter of string 's' as a new string
Example: If "Hello" is input, then the output is "Hlo"

mystery 2 will alternate between accumulating values from the start and
end of the string and printing them as one string
Example: If "Hello" is input, then the output is "HoelllleoH"

mystery 3 will print the number of times the string v is seen in string s
Example:
v = "H"
s = "Hello"
prints : "1"

mystery 4 will print all the elements seen directly after any
numeral values seen in string 's'
Example:
s = "Hello123"
prints: "23"

"""
s = input("Enter a string: ")
i = 1
acc = ""
while i < len(s):
    if s[i-1].isdigit():
        acc += s[i]
    i+=1
print(acc)
