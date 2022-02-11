import random
def func():
    print("Hello World")

def func1(name):
    print("Hi my name is {0}".format(name))
func1("Google")

def func3(x,y,z):
    if z:
        return x
    return y

def func4(x,y):
    return x * y

def is_even(param):
    if not param % 2:
        return False
    return True

def func5(x,y):
    if x > y:
        return True
    return False

def func6(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
func6(1,2,3)

def func7(*args):
    returnList = []
    for i in args:
        if not i % 2:
            returnList.append(i)

def func8(name):
    li = list(name)
    i = 0
    while i < len(li):
        if i % 2:
            li[i] = li[i].lower()
        else:
            li[i] = li[i].capitalize()
        i+=1
    
    print("".join(li))

func8("carlos")

def func9(num1,num2):
    if not num1 % 2 and not num2 % 2:
        if num1 < num2:
            return num1
        return num2
    if num1 > num2:
        return num1
    return num2

def func10(strOne, strTwo):
    str1 = list(strOne.lower())
    str2 = list(strTwo.lower())
    if(str1 == str2):
        return True
    return False

def func11(num):
    while(num >= 7):
        num = input("Please enter a valid number: ")
    gap = 7-num
    return gap+7
func11(input("Enter the number (must be less than 7): "))

def func12(str):
    toList = list(str)
    toList[0] = toList[0].capitalize()
    toList[3] = toList[3].capitalize()
    return "".join(toList)