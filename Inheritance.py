class A:
    a = 10
    def __init__(self, a):
        self.a = a

    def display(self):
        print('Value: {}'.format(self.a))

    def classAMethod(self):
        print('classAMethod')

class B:
    b = 20
    def __init__(self, b):
        self.b = b
    
    def display(self):
        print('Value: {}'.format(self.b))

    def classBMethod(self):
        print('classBMethod')

class C(A):
    c = 30
    def __init__(self, c):
        self.c = c

    # def display(self):
    #     print('Value: {}'.format(self.c))

    def classCMethod(self):
        print('classCMethod')

c = C(30)
print(c.a)
c.classAMethod()
c.display()


class Polygon:
    
    def __init__(self, numberOfsides):
        self.numberOfsides = numberOfsides
        self.sides = []
    
    def getSides(self):
        return self.sides

    def inputSides(self):
        i = 0
        while i < self.numberOfsides:
            side = int(input('Enter side {}: '.format(i+1)))
            self.sides.append(side)
            i += 1

    def getNumberOfsides(self):
        return self.numberOfsides

    def area(self):
        sumOfSides = 0
        for side in self.sides:
            sumOfSides += side
        print('Area of polygon: {}'.format(sumOfSides/2.0))


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)
    
    def area(self):
        sumOfSides = 0
        for side in self.sides:
            sumOfSides += side
        print('Area of Rectangle: {}'.format(sumOfSides/2.0))


class Square(Rectangle):
    def __init__(self):
        super().__init__()

    def area(self):
        print('Area of Square: {}'.format(self.sides[0]**2))



rect = Rectangle()
rect.inputSides()

rect.area()

sqr = Square()
sqr.inputSides()

sqr.area()

