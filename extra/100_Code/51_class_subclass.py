
class American(object):
    def printNationality(self):
        print("American")
        
class New_Yorker(American):
    def printNationality(self):
        print("New Yorker")
        
        
anAmerican = American()
aNewYorker = New_Yorker()
anAmerican.printNationality()
aNewYorker.printNationality()