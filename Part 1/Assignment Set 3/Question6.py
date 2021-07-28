'''
Created on Apr 23, 2021

@author: Karthik
'''
#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    total = 0
    for num in chocolates_received :
        total = total + num
    return total

def reward_child(child_id_rewarded,extra_chocolates):
    #Remove pass and write your logic here
    if (extra_chocolates<1):
        print("Extra chocolates is less than 1")
    elif child_id_rewarded not in child_id :
        print("Child id is invalid")
    else :
        if child_id_rewarded in child_id:
            z = child_id.index(child_id_rewarded)
            chocolates_received[z] = chocolates_received [z]+extra_chocolates
        print(chocolates_received)

print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)