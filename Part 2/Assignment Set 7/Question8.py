'''
Created on Jul 30, 2021

@author:  Karthik
'''
#lex_auth_01269445968039936095

def validate_credit_card_number(card_number):
    #start writing your code here
    num = card_number
    num = str(num)
    l1 = []
    l2 = []
    for i in range(len(num)) :
        if i%2 == 0 :
            z = int(num[i])
            z = z*2
            if len(str(z)) == 1 :
                l1.append(z)
            else :
                s = 0
                for i in str(z):
                    s += int(i)
                l1.append(s)
           
        else :
            l2.append(int(num[i]))
    s1 = sum(l1) 
    s2 = sum(l2)
    s = 0 
    s = s1+s2
    if s%10 == 0 :
        return True
    else :
        return False
card_number= 4539869650133101 #1456734512345698 #  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")