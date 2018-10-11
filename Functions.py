def functionName():
    print("functionName")

functionName()

def functionWith(param):
    print(param)

functionWith(100)

def functionWithTwo(param1, param2):
    print("Params: {} {}".format(param1, param2))

functionWithTwo(10, "Codekul")


def functionWithDefalut(param1, param2 = 100):
    print("Params: {} {}".format(param1, param2))

functionWithDefalut("Codekul", 50)

def functionWithReturning():
    return "Codekul"

print(functionWithReturning())

def changeThisNumber(number):
    print("Function before id: ",id(number))
    number = 50
    print("Function after id: ",id(number))

number = 10
print("Before: {}".format(number))
print("Before id: ",id(number))
changeThisNumber(number)
print("After: {}".format(number))
print("After id: ",id(number))


def changeThis(myList):
    print("Function before id: ",id(myList))
    # myList.append(10)
    myList.remove(4)
    myList.remove(5)
    # myList = [1,2,3]
    print("Function after id: ",id(myList))

myList = [1,2,3,4,5]
print("Before: {}".format(myList))
print("Before id: ",id(myList))
changeThis(myList)
print("After: {}".format(myList))
print("After id: ",id(myList))


def removeEverythingExceptString(strings):
    for s in strings:
        if not isinstance(s,str):
            strings.remove(s)


strings = ['One', 'Two', 3, 4, 'Red', 'Green', 'Blue', 23.60]
removeEverythingExceptString(strings)
print(strings)