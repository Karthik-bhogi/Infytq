'''
Created on Apr 23, 2021

@author: Karthik
'''
def find_leap_years(given_year):
    list_of_leap_years=[]
    # Write your logic here
    if(given_year%4==0):
        # list_of_leap_years= list_of_leap_years + [given_year]
        for new_year in range(0,61,4):
            new_leap_year = new_year+given_year
            if (new_leap_year %100 == 0  and new_leap_year %400 != 0 ):
                new_leap_year = new_leap_year + 4
                continue
            list_of_leap_years = list_of_leap_years + [new_leap_year]
        if(len(list_of_leap_years)>=15):
            list_of_leap_years=list_of_leap_years[:15]             
    elif(given_year%4==1):
        nearest_leap_year=given_year+3
        for new_year in range(0,60,4):
            new_leap_year = new_year+nearest_leap_year
            list_of_leap_years = list_of_leap_years +[new_leap_year]
    elif(given_year%4==2):
        nearest_leap_year=given_year+2
        for new_year in range(0,60,4):
            new_leap_year = new_year+nearest_leap_year
            list_of_leap_years = list_of_leap_years + [new_leap_year]
    elif(given_year%4==3):
        nearest_leap_year=given_year+1
        for new_year in range(0,60,4):
            new_leap_year = new_year+nearest_leap_year
            list_of_leap_years = list_of_leap_years + [new_leap_year]
    return list_of_leap_years

list_of_leap_years=find_leap_years(2001)
print(list_of_leap_years)