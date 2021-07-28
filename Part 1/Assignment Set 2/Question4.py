'''
Created on Apr 23, 2021

@author: Karthik
'''
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    ch=['N','V']
    bill_amount=0
    #write your logic here
    if(food_type != "N" and food_type !="V"):
        bill_amount=-1
        return bill_amount
    elif (distance_in_kms<1):
        bill_amount=-1
        return bill_amount
    elif(quantity_ordered<1):
        bill_amount=-1
        return bill_amount
    elif(food_type=="N"):
        if(distance_in_kms<=3):
            bill_amount=int(quantity_ordered)*150
            return bill_amount
        elif(3<distance_in_kms<=6):
            distance_in_kms=distance_in_kms-3
            bill_amount=quantity_ordered*150+(distance_in_kms)*3
            return bill_amount
        elif(distance_in_kms>6):
            distance_in_kms=distance_in_kms-6
            bill_amount=quantity_ordered*150+(distance_in_kms)*6+9
            return bill_amount
    elif(food_type=="V"):
        if(distance_in_kms<=3):
            bill_amount=quantity_ordered*120
            return bill_amount
        elif(3<distance_in_kms<=6):
            distance_in_kms=distance_in_kms-3
            bill_amount=quantity_ordered*120+(distance_in_kms)*3
            return bill_amount
        elif(distance_in_kms>6):
            distance_in_kms=distance_in_kms-6
            bill_amount=quantity_ordered*120+(distance_in_kms)*6+9
            return bill_amount
    else:
        return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,2)
print(bill_amount)