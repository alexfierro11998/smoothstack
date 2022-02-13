from ast import arg
from gc import callbacks


def bmiCalculator(people = 0):
    peopleData = list()
    resultData = list()
    i = 1
    while i <= int(people):
        data = input("Enter person #{iterator} (Enter with a gap between the weight(kilos) and height(meters)): ".format(iterator = i)).split()
        peopleData.append(data)
        i+=1
    for x in peopleData:
        calculation = float(x[0]) / float(x[1])**2
        if calculation < 18.5:
            resultData.append("under")
        elif 18.5 <= calculation < 25.0:
            resultData.append("normal")
        elif 25.0 <= calculation < 30.0:
            resultData.append("over")
        else:
            resultData.append("obese")
    print(" ".join(resultData))

    
bmiCalculator(input("Number of people? "))
