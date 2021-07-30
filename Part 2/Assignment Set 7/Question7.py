'''
Created on Jul 30, 2021

@author:  Karthik
'''
#lex_auth_012694465248329728100

#lex_auth_012694465248329728100

def validate_name(name):
    #Start writing your code here
    if len(name) >= 1 and len(name)<=15 :
        if str.isalpha(name) :
            return True
        else :
            return False
    else :
        return False

def validate_phone_no(phno):
    #Start writing your code here
    if len(str(phno))==10 :
        if str.isdigit(phno) :
            if len(set(str(phno))) == 1 :
                return False
            else :
                return True
        else :
            return False
    else :
        return False

def validate_email_id(email_id):
    #Start writing your code here
    if '@' and '.com' in email_id :
        if email_id[-4:] == '.com' :
            s = ''
            count = 0
            c1 = 0 
            c2 = 0
            for i in email_id :
                if i == '@' : c1 += 1
            if c1 > 1 : return False 
            for i in range(len(email_id)-3) :
                if email_id[i:i+4] == '.com' :
                    c2 += 1
            if c2 > 1 : return False
            if c1 == 1 and c2 ==1 :
                for i in email_id :
                    if i == '@' : break
                    else : count = count + 1
            if email_id[count:] == '@gmail.com' or email_id[count:] =='@yahoo.com' or email_id[count:] =='@hotmail.com' :
                return True 
            else :
                return False
    else :
        return False

def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    if validate_name(name) and validate_phone_no(phone_no) and validate_email_id(email_id) : print("All the details are valid")
    else :
        if not validate_name(name) : print("Invalid Name")
        if not validate_phone_no(phone_no) : print("Invalid phone number")
        if not validate_email_id(email_id) : print("Invalid email id")

#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")