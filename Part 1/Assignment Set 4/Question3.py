'''
Created on Apr 23, 2021

@author: Karthik
'''
def find_correct(word_dict):
    li=[]
    correct,almost_correct,wrong=0,0,0
    for word in word_dict:
        if len(word)>len(word_dict[word]) or len(word_dict[word])>len(word):
            wrong+=1
        else:
            a=0
            for i in range(len(max(word,word_dict[word]))):
                if word_dict[word][i]!=word[i]:
                    a+=1
            if a==0:
                correct+=1
            elif a==1 or a==2:
                almost_correct+=1
            else:
                wrong+=1
        
    return([correct,almost_correct,wrong])                   
                   
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))