'''
Created on Apr 23, 2021

@author: Karthik
'''
def check_palindrome(word):
    #Remove pass and write your logic here
    length = len(word)
    letter_list = ""
    n = 0
    while(length>n):
        letter_list = letter_list +" "+ word[n]
        n = n +1
    letter_list = letter_list[1:]
    letter_list=letter_list.split(" ")
    first = 0
    last = length-1
    while(length>0):
        if (letter_list[first] == letter_list[last]):
            first += 1
            last -= 1
            length = length - 1
            status = True
            continue 
        else:
            status = False
            break
    return status    

status=check_palindrome("malayalam")
if(status == True):
    print("word is palindrome")
else:
    print("word is not palindrome")