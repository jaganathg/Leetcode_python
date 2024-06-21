
class MyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    
    
if __name__ == "__main__":
    try:
        MyError("This is my custom error")
    except MyError as e:
        print(e)