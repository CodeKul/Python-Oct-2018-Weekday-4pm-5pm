class MyClass:
    str = 0
    def __init__(self, str):
        print("Object is created!")
        self.str = str
    
    def display(self):
        print(self.str)


# obj = MyClass('Codekul')
# obj.display()

class Vehicle:
    
    def __init__ (self, topSpeed, numberOfWheels):
        self.topSpeed = topSpeed
        self.numberOfWheels = numberOfWheels

    def moveForward(self):
        print('Moving forward...')
    
    def moveBackward(self):
        print('Moving backward...')

    def turnLeft(self):
        print('Turning left...')
    
    def turnRight(self):
        print('Turning right...')

    def getTopSpeed(self):
        return self.topSpeed

    def getNumberOfWheels(self):
        return self.numberOfWheels

    def updateTopSpeed(self, topSpeed):
        self.topSpeed = topSpeed
    
    def updateNumberOfWheels(self, numberOfWheels):
        self.numberOfWheels = numberOfWheels

v1 = Vehicle(100, 4)

v1.moveForward()
v1.moveBackward()
v1.turnLeft()
v1.turnRight()

print('Number of wheels: {}'.format(v1.getNumberOfWheels()))
print('Top speed: {}'.format(v1.getTopSpeed()))

v1.updateTopSpeed(200)
print('Top speed: {}'.format(v1.getTopSpeed()))

v1.topSpeed = 300
print('Top speed: {}'.format(v1.getTopSpeed()))



