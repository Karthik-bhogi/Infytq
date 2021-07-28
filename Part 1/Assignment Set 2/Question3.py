'''
Created on Apr 23, 2021

@author: Karthik
'''
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    
    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    five_needed = rupees_to_make // 5
    if(five_needed>no_of_five):
        five_needed = no_of_five
    one_needed = rupees_to_make - (five_needed*5)
    if(rupees_to_make > ((5*no_of_five) + (no_of_one)) or (one_needed>no_of_one)) :
        print(-1)
    else :
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)

#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
rupees_to_make=93
no_of_five=19
no_of_one=2
make_amount(rupees_to_make,no_of_five,no_of_one)     
