# Assignment Set 4 Questions

Click on the question numbers to redirect to the question webpage.

[1.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012693825794351104168_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course) Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.<br>
    **Note**: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.<br>
    
![q1](https://user-images.githubusercontent.com/64722906/127281827-580b2075-a7fa-4652-b266-ac29f88a3345.png)

[2.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269444195664691284_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course) Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message. <br>
    Words at odd position -> Reverse It <br>
    Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change <br>
    **Note:**
    1. Assume that the sentence would begin with a word and there will be only a single space between the words. <br>
    2. Perform case sensitive string operations wherever necessary. <br>

![q2](https://user-images.githubusercontent.com/64722906/127282031-de8fd540-0009-47aa-82a1-117a0c798da6.png)

[3.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269444890062848087_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course) Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.The input dictionary will contain correct spelling of     a word as key and the spelling provided by a contestant as the value.<br>

    The function should identify the degree of correctness as mentioned below:<br>
    CORRECT, if it is an exact match<br>
    ALMOST CORRECT, if no more than 2 letters are wrong<br>
    WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.<br>

    and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. Assume that the words contain only uppercase           letters and the maximum word length is 10.<br>

![q3](https://user-images.githubusercontent.com/64722906/127282143-5745747f-fcd4-4813-a1b7-a10bfa584a4e.png)


[4.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012693816757551104165_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course) Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality         visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:<br>
    {  <br>
    "P":"Pediatrics",<br>
    "O":"Orthopedics",<br>
    "E":"ENT<br>
    } <br>
    Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.<br>
    **Note**: <br>
    Assume that there is always only one medical speciality which is visited by maximum number of patients.<br>
    Perform case sensitive string comparison wherever necessary.<br>

![q4](https://user-images.githubusercontent.com/64722906/127282368-41d85101-6078-42f5-b517-2ef4d341208c.png)

[5.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269444961482342489_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course) Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. <br>
    Rules are as follows: <br>
    1. Spaces are to be retained as is <br>
    2. Each word should be encoded separately <br>
    If a word has only vowels then retain the word as is <br>
    If a word has a consonant (at least 1) then retain only those consonants <br>
    **Note**: Assume that the sentence would begin with a word and there will be only a single space between the words. <br>

![q5](https://user-images.githubusercontent.com/64722906/127282401-cdcc4e4a-0f9e-4359-9cae-8fd7884c3e2d.png)

[6.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_0127382283825971201450_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course) Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a           space.<br>
    **Rules**:<br>
    The word should have the largest frequency.<br>
    In case multiple words have the same frequency, then choose the word that has the maximum length.<br>
    **Assumptions**:<br>
    The text has no special characters other than space.
    The text would begin with a word and there will be only a single space between the words.<br>
    Perform case insensitive string comparisons wherever necessary.<br>
    
![q6](https://user-images.githubusercontent.com/64722906/127282426-7415e29f-4f0a-4ebf-a4cc-7c59480ebade.png)
