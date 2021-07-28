'''
Created on Apr 23, 2021

@author: Karthik
'''
def max_frequency_word_counter(data):
    li=data.lower().split()
    dick={}
    for word in li:
        count=0
        for i in range(len(li)):
            if li[i]==word:
                count+=1
        dick[word]=count
    
    words=[]
    frequency=[]
    for word in dick:
        words.append(word)
        frequency.append(dick[word])

    a=max(frequency)
    for i in range(len(words)):
        if frequency[i]==a:
            b=words[i]
    
    a=max(frequency)
    temp=[]
    
    for i in range(len(words)):
        if frequency[i]==a:
            temp.append(words[i])

    max_len=-1
    for ele in temp:
        if len(ele)>max_len:
            max_len=len(ele)
            out=ele
    print(ele, a)
data="data-Listen to on on the big clock Tick tock tick"
max_frequency_word_counter(data)