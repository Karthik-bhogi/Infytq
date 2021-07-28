'''
Created on Apr 23, 2021

@author: Karthik
'''
def create_largest_number(number_list):
    #remove pass and write your logic here
    number_list.sort()
    number = []
   # print(number_list)
    for num in number_list :
        number = [num] + number
   # print(number)
    n=len(number_list)
    n =2*n
    largest_number = 0
    for num in number :
        largest_number1 = num * (10**(n-2))
        largest_number = largest_number + largest_number1
        n = n-2
    return largest_number

number_list=[23,85,67]
largest_number=create_largest_number(number_list)
print(largest_number)