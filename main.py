import cl_Points as Point
import cl_Lines as Line
import cl_Unit as Unit
Point_1 = Point.Point(-6, 7)
Point_2 = Point.Point(-6, 7)
Point_3 = Point.Point(20, 10)
print(Point_1)
print(Point_1.Equal(Point_2))  # Equal
print(Point_1.Equal(Point_3))  # not equal
print("*" * 100)

Line_1 = Line.Line(Point_1, Point_3)
#Line_2 = Line.Line(Point_1, Point_2)
print("Point one:", Line_1.Point_start)
print("Point two:", Line_1.Point_end)
print("*" * 100)
print(Line_1)
#print(Line_2)
print("*" * 100)

Bob = Unit.Unit("Bob", 10, 18, 1)
print(Bob)
print("*"*100)
Georg = Unit.Unit("Georg", 10, 1, 2)
print(Georg)
print("*"*100)
Bob.Hit(Georg)