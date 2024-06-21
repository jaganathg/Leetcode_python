
class MyClass:
    name = 'Person'
    
    def __init__(self, name):
        self.name = name
        
if __name__ == '__main__':
    jagan = MyClass('Jagan')
    print(f"{MyClass.name} and {jagan.name}")
    
    nithya = MyClass()
    nithya.name = 'Nithya'
    print(f"{MyClass.name} and {nithya.name}")
    