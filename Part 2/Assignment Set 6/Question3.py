'''
Created on Jul 28, 2021

@author: Karthik
'''
def find_duplicates(list_of_numbers):
    #start writing your code here
    x = []
    y = []
    for i in list_of_numbers :
        if i in x :
            y += [i]
        else :
            x += [i]
    return list(set(y))

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)