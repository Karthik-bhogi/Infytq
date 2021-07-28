'''
Created on Apr 23, 2021

@author: Karthik
'''

def solve(heads,legs):
    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if(heads>legs or legs > 4*heads or legs%2 ==1):
        print(error_msg)
    elif(legs == 2*heads):
        chicken_count=heads
        rabbit_count=0
        print(chicken_count,rabbit_count)
    elif(legs==4*heads):
        chicken_count=0
        rabbit_count=heads
        print(chicken_count,rabbit_count)
    elif(2*heads<legs<4*heads):
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))
    else:
        print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,132)