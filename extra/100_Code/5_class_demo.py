class test_class():
    def __init__(self):
        self.name = ""
    def getString(self):
        self.name = input()
    def printString(self):
        print(self.name.upper ())
        
myClass = test_class()
myClass.getString()
myClass.printString()