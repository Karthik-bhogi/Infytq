'''
Created on Jul 30, 2021

@author: Karthik
'''
#lex_auth_01269443664174284882
def reverse(num):
    return str(num)[::-1]
    
def nearest_palindrome(number):
    #start writitng your code here
    while(1):
        number += 1
        if str(number)==reverse(number):
            return number
            break

number=99
print(nearest_palindrome(number))