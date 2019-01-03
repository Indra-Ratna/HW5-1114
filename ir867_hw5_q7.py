#Indra Ratna
#CS-UY 1114
#12 Oct 2018
#Homework 5
#Problem 7

needle = input("Enter needle: ")
haystack = input("Enter haystack: ")
pos = -1
i = 0
while i < len(haystack):
    if(haystack[i:i+len(needle)]==needle):
        pos = i
        break
    else:
        i+=1
if(pos!=-1):
    print("Needle found in haystack at position "+str(pos))
else:
    print("Needle not found in haystack")
