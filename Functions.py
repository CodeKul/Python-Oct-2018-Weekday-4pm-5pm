'''
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


def removeEverythingExceptString1(strings):
    count = 0
    for (i, s) in enumerate(strings):
        if not isinstance(s,str):
           strings[i] = 0
           count += 1
    while count > 0:
        strings.remove(0)
        count -= 1

def removeEverythingExceptString2(strings):
    count = len(strings) - 1
    while count >  0:
        if not isinstance(strings[count],str):
            strings.remove(strings[count])
        count -= 1

strings = ['One', 'Two', 3, 4, 'Red', 'Green', 'Blue', 23.60, 56, 36.98]
removeEverythingExceptString2(strings)
print(strings)

'''


def calcSeries(list):
        degree = 1
        sum = 0
        for num in list:
               sum += (num**degree)
               degree += 1
        return sum

def inputList(list):
        while True:
                num = int(input('Enter number: '))
                if num == 0:
                    break
                else:
                        list.append(num)


list = []
inputList(list)
print(list)
print(calcSeries(list))

def sumOfList(list):
        sum = 0
        for num in list:
                sum += num
        return sum

print(sumOfList(list))

def splitTheList(list):
        length = len(list)
        mid = int(length/2.0)
        print(type(mid))
        list1 = []
        list2 = []
        for i,num in enumerate(list):
                if i < mid:
                        list1.append(num)
                else:
                        list2.append(num)
        return list1, list2

print(splitTheList(list))