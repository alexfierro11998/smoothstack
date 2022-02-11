import math

print("Hello World"[8])

print("thinker"[2:5])

#Question 3: answer is 'mmy'

"""input data:
3 <== palindrome
Stars <== not a palindrome
O, a kak Uwakov lil vo kawu kakao! <== palindrome
Some men interpret nine memos <== not a palindrome 
"""

palindromeList = ["3", "stars", "O, a kak Uwakov lil vo kawu kakao!","Some men interpret nine memos" ]

def palindromeDetector(palindrome):
    if(len(palindrome) == 1):
        return "Y"
    palindrome = palindrome.replace(" ","")
    palindrome = palindrome.replace("!","")
    palindrome = palindrome.replace(",","")
    palindrome = palindrome.lower()
    middle = math.floor(len(palindrome) / 2) + 1
    i = 0
    while i < middle:
        if palindrome[i] != palindrome[len(palindrome) - 1 - i]:
            return "N"
        i += 1
           
    return "Y"
   




for x in palindromeList:
    print(palindromeDetector(x))

