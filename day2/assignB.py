numberSet = {42, "Word", 42.42}
print(numberSet)

sample = [1,1,[1,2]]
print(sample[2][1])

lst = ['a','b','c']
#['b','c']

weekdays = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday" : 5, "Saturday": 6}

D={'k1':[1,2,3]}
#output is 2

listToTuple = (1,(2,3))
print(listToTuple)

word = set("Mississippi")
print(word)

#Can you add an element 'X' into set above? Yes, with add method

#output of set([1,1,2,3]) = 1,2,3

setOfNumbers = set()
rangeOfNumbers = range(2000,3201)
for i in rangeOfNumbers:
    if not(i % 7) and i % 5:
        setOfNumbers.add(i)
print(setOfNumbers)

def factorialize(n):
    if n == 1:
        return n
    return n * factorialize(n - 1)
print(factorialize(5))

def integralize(n):
    newDictionary = {}
    for currentNum in range(1,n + 1):
        squared = currentNum ** 2
        newDictionary[currentNum] = squared
    print(newDictionary)
integralize(8)

def inputConverter(input):
    print(input.split(","))
    print(tuple(input.split(",")))
inputConverter(input())

class testClass:
    def __init__(self):
        self.input = ""
    def getString(self):
        self.input = input("Enter input: ")
        while not len(self.input):
            self.input = input("Please enter valid input: ")
    def printString(self):
        if(not len(self.input)):
            self.input = input("Please enter a string (To prevent this execute getString() first): ")
            print("Output: " + self.input)
        else:
            print("Output: " + self.input)
newClass = testClass()
newClass.printString()