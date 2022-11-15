import cl_Points as Point
# 2.Модифицируйте класс Line следующим образом:
#   -  обеспечьте проверку точек начала и конца при создании линии в __init__
#   (точки начала и конца отрезка не должны совпадать)
#   -  создайте метод __str__ . он должен отдавать информацию в формате
#   ("Line with points [информация о точке начала] [информация о точке конца] and length [длина]")
class Line:
    _Point_start = None
    _Point_end = None

    def __init__(self, start, end):
        if isinstance(start, Point.Point) or isinstance(end, Point.Point):
            if start.Equal(end):
                raise TypeError
            self._Point_start = start
            self._Point_end = end

    @property
    def Point_start(self):
        return self._Point_start

    @property
    def Point_end(self):
        return self._Point_end

    def Length(self):
        return (((self.Point_start.x + self.Point_end.x) - (self.Point_start.y + self.Point_end.y))**2)**0.5

    def __str__(self):
        return f"Line with point one: {self.Point_start.x , self.Point_start.y}, point two: {self.Point_end.x, self.Point_end.y} and their length {self.Length()}"
