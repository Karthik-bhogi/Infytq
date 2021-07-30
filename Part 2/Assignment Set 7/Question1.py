'''
Created on Jul 28, 2021

@author: Karthik
'''
def check_anagram(data1,data2):
    #start writing your code here
    data1 = data1.lower()
    data2 = data2.lower()
    if len(data1) != len(data2):
        return False
    else:
        l1 = []
        l2 = []
        for i in range(len(data1)) :
            if data1[i]==data2[i]:
                return False
            else :
                l1 += data1[i]
                l2 += data2[i]
        if sorted(l1) == sorted(l2):
            return True
        else :
            return False


print(check_anagram("eat","tea"))