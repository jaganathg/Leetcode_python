

class gen:
    def __init__(self, num) -> None:
        self.num = num
        print("I'm Gen")
    
    def putNumber(self):
        i = 0
        while i < self.num:
            j = i
            i += 1
            if j % 7 == 0:
                yield j
                
                
if __name__ == "__main__":
    g = gen(96)
    for i in g.putNumber():
        print(i)