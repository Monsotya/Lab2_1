class Rational:

    def __init__(self, numerator=1, denominator=1):
        a = numerator
        b = denominator
        if b == 0:
            raise ZeroDivisionError
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        if a + b != 0:
            numerator /= (a + b)
            denominator /= (a + b)
        self._numerator = numerator
        self._denominator = denominator

    def print_fraction(self):
        print(self._numerator, " / ", self._denominator)

    def print_result(self):
        print(self._numerator / self._denominator)


try:
    object = Rational(2, 0)
    object.print_fraction()
    object.print_result()
except ZeroDivisionError:
    print("Error!\n")
