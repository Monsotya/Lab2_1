from math import gcd

class Rational:

    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int):
            raise TypeError
        if not isinstance(denominator, int):
            raise TypeError
        if not denominator:
            raise ValueError
        self._numerator = numerator // gcd(numerator, denominator)
        self._denominator = denominator // gcd(numerator, denominator)

    def fraction(self):
        return f'{self._numerator} / {self._denominator}'

    def result(self):
        return self._numerator / self._denominator


try:
    object = Rational(3, 6)
    print(object.fraction())
    print(object.result())
except TypeError:
    print("Wrong type!\n")
except ValueError:
    print("Zero division!\n")
