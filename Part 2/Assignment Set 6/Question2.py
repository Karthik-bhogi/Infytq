'''
Created on Jul 28, 2021

@author: Karthik
'''
import math
def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    #Accepts the list of factors and returns the largest prime factor
    l=[]
    for i in list_of_factors :
        i = find_f(i)
        l += [i]  
    return max(l)

def find_f(num):
    #Accepts the number and returns the largest prime factor of the number
    g = 0
    while num % 2 == 0:
        g = 2
        num /= 2     
         
    while num % 3 == 0:
        g = 3
        num = num/3

    for i in range(5, int(num)+1):
        while num % i == 0:
            g = i
            num = num / i
        while num % (i+2) == 0:
            g = i+2
            num = num / (i+2)
    return g

def find_g(num):
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    sumo = 0
    for i in range(num,num+9):
        if is_prime(i,i//2):
            sumo += i
        else :
            l = find_factors(i)
            a = find_largest_prime_factor(l)
            if is_prime(a,a//2):
                sumo += a
            else :
                b = find_f(a)
                sumo += b
    return sumo
            
#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))