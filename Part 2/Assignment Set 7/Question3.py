'''
Created on Jul 28, 2021

@author: karthik
'''
def check_perfect_number(number):
    #start writing your code here
    l = []
    if number==0:
        return False
    for i in range(1,int(number/2)+1):
        if number%i == 0:
            l+=[i]
        else :
            continue
    if sum(l)==number :
        return True
    else :
        return False

def check_perfectno_from_list(no_list):
    #start writing your code here
    a=[]
    for i in no_list :
        if check_perfect_number(i):
            a.append(i)
        else:
            continue
    return a

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)