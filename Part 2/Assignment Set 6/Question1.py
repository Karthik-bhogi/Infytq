'''
Created on Jul 28, 2021

@author: Karthik
'''
def is_palindrome(word):
    #Remove pass and write your logic here
    word = word.upper()
    if len(word)<= 1 :
        return True
    else :
        if word[0]==word[-1]:
            return is_palindrome(word[1:-1])
        elif (word[0] != word[1]) :
            return False
        else :
            return False
#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
