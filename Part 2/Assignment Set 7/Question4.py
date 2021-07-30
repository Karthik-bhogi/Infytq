'''
Created on Jul 28, 2021

@author: Karthik
'''
#lex_auth_0127382193364008961449

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]
d = {}

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    count = 0
    for i in ticket_list :
        if destination in i[10:13] :
            count += 1
        else :
            continue
    return count
    #Remove pass and write your logic here

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    l = []
    for i in ticket_list :
        if i[0:5] not in l :
            l.append(i[0:5])
        else : continue
    for i in l :
        count = 0
        for j in ticket_list :
            if i in j :
                count = count + 1
            d[i]=count
    a = []
    for key in d :
        a += [key+str(':')+str(d[key])]
    return a
    #Remove pass and write your logic here

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    a = find_passengers_per_flight()
    b = []
    e = []
    for i in a :
        b += i[6] 
    b = sorted(b)
    b = b[::-1]
    for i in b :
        for j in a :
            if i in j[6] :
                e += [j]
    return e
    #Remove pass and write your logic here

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())