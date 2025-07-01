
class Phone:
    def __init__(self):
        self.model = ""
        self.ram = 0
        self.brand = ""
        self.operatingSystem = ""
    def printResults(self):
        print("You have an "+ self.model)
myPhone = Phone()
myPhone.model = "iPhone 14"
myPhone.ram = 6
myPhone.brand = "Apple"
myPhone.operatingSystem = "iOS"

myPhone.printResults()

class Subtraction:
    def __init__(self, number1,number2):
        self.number1 = number1
        self.number2 = number2
    def subtract(self):
        print(self.number1 - self.number2)
result = Subtraction(2,2)
result.subtract()