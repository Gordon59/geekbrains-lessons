# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.

# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt

class Trg:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

    def S(self, a, h):
        return 'S = ', a*h*0.5

    def H(self, a, b, c):
        p = 0.5 * (a + b + c)
        num = 2 * (sqrt(p*(p-a)*(p-b)*(p-c)))
        return 'H к стороне a = ', num / a
        return 'H к стороне b = ', num / b
        return 'H к стороне c = ', num / c

    def P(self, a, b, c):
        return a + b + c

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.

# Предусмотреть в классе методы:

# проверка, является ли фигура равнобочной трапецией;

# вычисления: длины сторон, периметр, площадь.

class RTrap:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy

    def RTrapt(self, ab, cd):
        if ab == cd:
            return "Трапеция равнобочная"



