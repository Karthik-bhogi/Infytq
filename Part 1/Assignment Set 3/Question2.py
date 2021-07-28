'''
Created on Apr 23, 2021

@author: Karthik
'''
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    gems = []
    required = []
    #Write your logic here
    for  a in gems_list :
        gems = gems + [a]
        b = gems_list.index(a)
        price = price_list[b]
        gems = gems + [price]
    for  c in reqd_gems :
        required = required + [c]
        d = reqd_gems.index(c)
        quantity = reqd_quantity[d]
        required = required + [quantity] 
    print(gems,required)
    l = len(reqd_quantity)
    print(l)
    count = 0
    while(l>count):
        if reqd_gems[count] in gems_list :
            z=gems_list.index(reqd_gems[count])
            bill_amount = bill_amount + reqd_quantity[count]*price_list[z]
            print(bill_amount)
        else:
            return -1
        count=count+1
    if (bill_amount>30000):
        bill_amount = 0.95 * bill_amount
    return bill_amount
    
#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[1,1,1,1,1]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)