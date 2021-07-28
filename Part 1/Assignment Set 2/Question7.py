'''
Created on Apr 23, 2021

@author: Karthik
'''
def find_max(num1, num2):
    # # Write your logic here
    # return max_num
    #Provide different values for num1 and num2 and test your program.
    # check for invalid data: 'num1' and 'num2' should be integers
    if type(num1) != int or type(num2) != int:
        return -1
    # check if 'num1' is greater than 'num2'
    if num1 >= num2:
        return -1
    # initialize empty list
    num_list = []
    # find the nearest multiple of 15 to 'num1'
    if num1 % 15 == 0:
        nearest_multiple = num1
    else:
        nearest_multiple = num1 + 15 - num1 % 15
    # scan through possible numbers from 'nearest_multiple' to 'num2'
    for numbers in range(nearest_multiple, num2 + 1, 15):
        if 10 <= numbers <= 99 or -99 <= numbers <= -10:
            num_list.append(numbers)
    # if no valid number was detected, the list will remain empty
    if num_list == []:
        return -1
    return max(num_list)
    
max_num=find_max(10,15)
print(max_num)