# Assignment Set 7 Questions

Click on the question numbers to redirect to the question webpage.

[1.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_0127382206342184961397_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course) Write a python function, check_anagram() which accepts two strings and returns True, if one string is a special anagram of another string. Otherwise returns False. <br>

The two strings are considered to be a special anagram if they contain repeating characters but none of the characters repeat at the same position. The length of the strings should be the same.<br>

**Note :** Perform case insensitive comparison wherever applicable.<br>

![q1](https://user-images.githubusercontent.com/64722906/127647581-6b149d51-49dc-43cc-87eb-f3fc3c253cf3.png)

[2.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269446319507046499_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course) Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given string and return it.<br>

![q2](https://user-images.githubusercontent.com/64722906/127647733-2effa665-8761-484b-bc48-55cb5d6bbf0d.png)

[3.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269446533799116898_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course) Write a python function to check whether the given number is a perfect number or not. The function should returns true if the number is a perfect number, else it should returns false.<br>
**Hint :** Perfect number is a positive whole number that is equal to the sum of its proper divisors.<br>
The first perfect number is 6 as the sum of its proper positive divisors, 1,2 and 3 is 6. Other perfect numbers are 28, 496, 8128 ... <br>

Extend the program written for the above problem to write another function to find all perfect numbers in a given list of numbers. Populate the perfect numbers in a list and return the list. If no perfect numbers found, return an empty list.<br>

**Note :** Reuse the code wherever possible.<br>

[4.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_0127382193364008961449_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course) Write a python program to help an airport manager to generate few statistics based on the ticket details available for a day.<br>
Go through the below program and complete it based on the comments mentioned in it.<br>

**Note :** Perform case sensitive string comparisons wherever necessary.<br>

[5.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269443664174284882_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course) Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number.Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number.<br>

![q5](https://user-images.githubusercontent.com/64722906/127648264-2ed41eab-e544-4df4-9bfd-4a9d8c8d1765.png)

[6.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269446157664256093_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course) The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.<br>

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.<br>

Write a python program to find and display the number of circular primes less than the given limit. <br>

[7.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012694465248329728100_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course) Write a python program to validate the details provided by a user as part of registering to a web application.<br>

Write a function validate_name(name) to validate the user name<br>
1. Name should not be empty, name should not exceed 15 characters<br>
2. Name should contain only alphabets<br>

Write a function validate_phone_no(phoneno) to validate the phone number<br>
1. Phone number should have 10 digits<br>
2. Phone number should not have any characters or special characters<br>
3. All the digits of the phone number should not be same.<br>
4. Example: 9999999999 is not a valid phone number<br>

Write a function validate_email_id(email_id) to validate email Id<br>
1. It should contain one '@' character and '.com'<br>
2. '.com' should be present at the end of the email id.<br>
3. Domain name should be either 'gmail', 'yahoo' or 'hotmail'<br>
**Note :** Consider the format of email id to be username@domain_name.com<br>

All the functions should return true if the corresponding value is valid. Otherwise, it should return false.<br>

Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the arguments passed to it and display appropriate message. Refer the comments provided in the code.<br>

**Note :** You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.<br>

[8.](https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_01269445968039936095_shared?collectionId=lex_auth_012734003600908288382_shared&collectionType=Course) Use Luhn algorithm to validate a credit card number.<br>

A credit card number has 16 digits, the last digit being the check digit. A credit card number can be validated using Luhn algorithm as follows:<br>

**Step 1a :** From the second last digit (inclusive), double the value of every second digit.<br>
Suppose the credit card number is 1456734512345698.<br>
Take the double of 9,5,3,1,4,7,5 and 1<br>
i.e., 18, 10, 6, 2, 8, 14, 10 and 2<br>

**Note :** If any number is greater than 9, then sum the digits of that number.<br>
i.e., 9, 1, 6, 2, 8, 5 ,1 and 2<br>

**Step 1b :** Sum the numbers obtained in Step 1a.<br>
i.e., 34<br>

**Step 2 :** Sum the remaining digits in the credit card and add it with the sum from Step 1b.<br>
i.e., 34 + (8+6+4+2+5+3+6+4) = 72<br>

**Step 3 :** If the total is divisible by 10 then the number is valid else it is not valid.<br>

Write a function, validate_credit_card_number(), which accepts a 16 digit credit card number and returns true if it is valid as per Luhn’s algorithm or false, if it is invalid. <br>
