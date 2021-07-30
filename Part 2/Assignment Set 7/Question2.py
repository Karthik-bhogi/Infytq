'''
Created on Jul 28, 2021

@author: karthik
'''
def remove_duplicates(value):
    #start writing your code here
    s = ''
    for i in value :
        if i not in s :
            s+=i
        else :
            continue
    return s

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))