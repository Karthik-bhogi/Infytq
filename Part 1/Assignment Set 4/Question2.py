'''
Created on Apr 23, 2021

@author: Karthik
'''
def encrypt_sentence(sentence):
    vowel=set("AEIOUaeiou")
    s1=sentence
    var=""

    li = list(sentence.split(" "))
    for i in range(len(li)):
        var=li[i]
        if(i%2==0):
            var=var[::-1]
            li[i]=var

        else:
            t=""
            t2=""
            for j in var:
                if(j in vowel):
                    t2=t2+j
                else:
                    t=t+j
            t=t+t2
            li[i]=t
    var2=""
    for i in range(len(li)):
        var2=var2+li[i]
        if(i != len(li)-1):
            var2=var2+" "
    return var2


sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)