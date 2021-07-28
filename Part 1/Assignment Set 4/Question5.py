'''
Created on Apr 23, 2021

@author: Karthik
'''
def sms_encoding(data):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    li=data.split()
    out=[]
    for word in li:
        s=""
        if len(word)==1:
            out.append(word)
        else:
            for char in word:
                if char not in vowels:
                    s+=char
            out.append(s)
    return(" ".join(out))
                
    #start writing your code here

data="I love Python"
print(sms_encoding(data))