class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def find_area(points):
    area = 0
    for i in range(len(points)-1):
        area+=(points[i+1].Y+points[i].Y)*(points[i+1].X-points[i].X)/2
    return area


if __name__=="__main__":
    print(find_area([Point(0,0), Point(1,4), Point(3,2)]))