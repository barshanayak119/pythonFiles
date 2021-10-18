# The following code will help us to determine the number of vowels in a string.

name = input("Enter your word: ")
i = 0
count = 0
k = len(name)
while(i<k):
    if(name[i] == "A") or (name[i] == "a") or( name[i] == "E") or (name[i] == "e") or (name[i] == "I") or (name[i] == "i") or (name[i]=="O") or (name[i] == "o") or (name[i] == "U") or (name[i] == "u"):
        count = count+1
    i=i+1
print("Total number of vowels in the word " + name + " is = " + str(count))
