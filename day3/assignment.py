import random
import sys
import math

def divisible():
    numberSet = set()
    for i in range(1500,2701):
        if not i % 7 and not i % 5:
            numberSet.add(i)
divisible()

def temperatureConverter(temperature, type):
    
    while type.lower() != "celsius" and type.lower() != "farenheit":
        print(type)
        print(type.lower())
        print(type == type.lower())
        type = input("Please check your spelling or enter a valid parameter (celsius or farenheit): ")
    type = type.lower()
    degree_sign = u"\N{DEGREE SIGN}"
    if(type.lower() == "celsius"):
        converted = 5 * ((int(temperature) - 32) / 9)
        print(f'{temperature}{degree_sign}F is {int(converted)}{degree_sign}C')
    elif(type.lower() == "farenheit"):
        converted = ((9 * int(temperature)) / 5) + 32
        print(f'{temperature}{degree_sign}C is {int(converted)}{degree_sign}F')

temperatureConverter(input("Please enter temperature: "), input("What are you converting to? "))


def guesser():
    guess = input("Enter your guess: ")
    variable = random.randint(1,9)
    while int(guess) != variable:
        guess = input("Guess again: ")
    print("Well guessed!")
guesser()

def drawer(size):
    for i in range(size * 2 - 1):
        stars = "*"
        if int(i) > size - 1:
            z = 1
            while z < size:
                stars += "*"
                z += 1 
            for k in range((int(i) - (size+1))+2):
                stars = stars[:-1]
        else:
            for j in range(i):
                stars += "*"      
        print(stars)
drawer(100)
#I was able to get this function to work with dynamic input :)

def reverser(word):
    converted = list(word)
    if len(word) <= 3: 
        first = converted[0]
        second = converted[-1]
        converted[-1] = first
        converted[0] = second
        return converted
    nextString = reverser("".join(converted[1:len(word) - 1]))
    i = 0
    j = 1
    while(i < len(nextString)):
        converted[j] = nextString[i]
        i+=1
        j+=1
    first = converted[0]
    second = converted[-1]
    converted[0] = second
    converted[-1] = first
    return "".join(converted)
print(reverser(input("Please input the word you want to reverse: ")))

def evenAndOdd(numbers):
    even = 0
    odd = 0
    for value in numbers:
        if value % 2:
            even += 1
        else:
            odd += 1
    print(f"Even numbers: {even}")
    print(f"Odd numbers: {odd}")
evenAndOdd((1,2,3,4,5,6,7,8,9))

def typeDeterminer(content):
    for i in content:
        print(type(i))
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
typeDeterminer(datalist)

def skipThreeAndSix(content):
    for i in content:
        if int(i) == 3 or int(i) == 6:
            continue
        print(i)
skipThreeAndSix([0,1,2,3,4,5,6])