class Drob:
    '''
    1. Конструктор по умолчанию должен создавать дробь с числителем 0 и знаменателем 1.
    2. При конструировании объека класса Drob с параметрами p и q
    должно выполняться сокращение дроби p/q (здесь вам может пригодиться решение задачи «Наибольший общий делитель»).
    3. Если дробь p/q отрицательная, то объект Drob(p, q) должен иметь
    отрицательный числитель и положительный знаменатель.
    4. Если дробь p/q положительная, то объект Drob(p, q) должен иметь положительные
    числитель и знаменатель (обратите внимание на случай Drob(-2, -3)).
    5. Если числитель дроби равен нулю, то знаменатель должен быть равен 1.
    6. При попыте создать объект со знаменателем равным 0, должно генерироваться исключение
    TypeError с соответствующим сообщением
    7. Реализовать перегрузку опреаторов +, -, *, /, чтобы можно было работать с дробями
    естественным образом:
    a = Drob(1,2)
    b = Drob(5,6)
    c = Drob()
    c = a + b
    8. Со списком дробей должны работать стандартный метод сортировки, функция max():
    lst = [Drob(1,3), Drob(4,1), Drob(6,4)]
    lst.sort()
    print(max(lst))
    '''

    class Drob:
        def __init__(self, p=0, q=1):
            if q == 0:
                raise TypeError("Знаменатель не может быть равен нулю")
            self.p = p
            self.q = q
            self.reduce()

        def reduce(self):
            gcd = self.gcd(abs(self.p), abs(self.q))
            self.p //= gcd
            self.q //= gcd
            if self.q < 0:
                self.p = -self.p
                self.q = -self.q

        def gcd(self, a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def __str__(self):
            return f"{self.p}/{self.q}"

        def __add__(self, other):
            if isinstance(other, Drob):
                p = self.p * other.q + other.p * self.q
                q = self.q * other.q
                return Drob(p, q)
            else:
                raise TypeError("Невозможно сложить объекты разных типов")

        def __sub__(self, other):
            if isinstance(other, Drob):
                p = self.p * other.q - other.p * self.q
                q = self.q * other.q
                return Drob(p, q)
            else:
                raise TypeError("Невозможно вычесть объекты разных типов")

        def __mul__(self, other):
            if isinstance(other, Drob):
                p = self.p * other.p
                q = self.q * other.q
                return Drob(p, q)
            else:
                raise TypeError("Невозможно умножить объекты разных типов")

        def __truediv__(self, other):
            if isinstance(other, Drob):
                p = self.p * other.q
                q = self.q * other.p
                return Drob(p, q)
            else:
                raise TypeError("Невозможно поделить объекты разных типов")

        def __lt__(self, other):
            if isinstance(other, Drob):
                return self.p * other.q < other.p * self.q
            else:
                raise TypeError("Невозможно сравнить объекты разных типов")

        def __gt__(self, other):
            return other < self

        def __le__(self, other):
            return self < other or self == other

        def __ge__(self, other):
            return self > other or self == other

        def __eq__(self, other):
            if isinstance(other, Drob):
                return self.p * other.q == other.p * self.q
            else:
                return False

        def __ne__(self, other):
            return not self == other

    lst = [Drob(1, 3), Drob(4, 1), Drob(6, 4)]
    lst.sort()
    print(max(lst))


