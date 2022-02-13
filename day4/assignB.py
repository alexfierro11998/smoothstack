def interpreter(data):
    func = lambda x: (x[0], f"{round(x[3] * x[2] + 10,2)}€") if (x[3] * x[2] < 100) else (x[0], f"{round(x[3] * x[2],2)}€")
    result = map(func, data)
    #print(list(result))
    
dataOne =[34587, "Learning Python, Mark Lutz", 4, 40.95]
dataTwo = [98762, "Programming Python, Mark Lutz", 5, 56.80]
dataThree = [77226, "Head First Python, Paul Barry", 3,32.95]
dataFour = [88112,"Einführung in Python3, Bernd Klein", 3, 24.99]
interpreter([dataOne,dataTwo,dataThree,dataFour])


def interpreter2(data):
    formatted = list()
    for x in data:
        i = 0
        sum  = 0
        while i < len(x):
            if(isinstance(x[i], tuple)):
                sum += x[i][1] * x[i][2]
                if(sum < 100):
                    sum *= .9
            i+=1
        formatted.append([x[0], sum])
    print(formatted)
    result = map(lambda x: x, data)
    print(result)
    
    

data1 = [34587, ("Learning Python, Mark Lutz", 4, 40.95),("Programming Python, Mark Lutz", 5, 56.80)]
data2 = [98762,("Head First Python, Paul Barry", 3, 32.95), ("Einführung in Python3, Bernd Klein",3,24.99)]
interpreter2([data1,data2])