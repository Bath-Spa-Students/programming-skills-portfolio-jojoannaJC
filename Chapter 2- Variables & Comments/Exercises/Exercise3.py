#Tidy up the code to make it easier to understand
#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
#Make sure you use each character combination, “\t” and “\n”, at least once.
#Print the name once, so the whitespace around the name is displayed. 
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().


l="\t Hello! n\ how are you? n\ hope you are good, t\ thanks!"
print(l)
print(l.lstrip())
print(l.rstrip())
print(l.strip())