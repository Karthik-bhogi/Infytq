'''
Created on Jul 30, 2021

@author:  Karthik
'''
#lex_auth_01269446157664256093

def check_prime(number):
    #remove pass and write your logic here. if the number is prime return true, else return false
    if number > 1 :
        for i in range(2,int(number/2)+1):
            if number % i ==0:
                return False
                break
        else :
            return True
    else :
        return False
        

def rotations(num):
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
    #Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
    l = []
    a = num
    for i in range(len(str(num))):
        s = ''
        if i == 0 :
            l.append(num)
        else :
            s += str(num)[1:]+str(num)[0]
            l.append(int(s))
            num = s
    return l

def get_circular_prime_count(limit):
    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    l = 0
    l1 = []
    for i in range(limit):
        if check_prime(i):
            l1 = rotations(i)
            c = 0
            for j in l1 :
                if check_prime(j) :
                    c += 1
                    continue
                else :
                    break
            if len(str(i)) == c :
                l = l+1
            else :
                continue
    return l

#Provide different values for limit and test your program
print(get_circular_prime_count(200))