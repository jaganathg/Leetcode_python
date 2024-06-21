
def zero_div():
    try:
        a = 5 / 0
    except ZeroDivisionError:
        print("Zero Division Error")
    finally:
        print("Successfully Divided")
        
if __name__ == "__main__":
    zero_div()