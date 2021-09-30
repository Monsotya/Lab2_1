class Rectangle:

    def __init__(self, length=1, width=1):
        self._width = width
        self._length = length

    def get_attributes(self):
        return self._width, self._length

    def set_attributes(self, length=1, width=1):
        if 0.0 < length < 20.0:
            self._length = length
        else:
            print("Error!\n")
            exit()
        if 0.0 < width < 20.0:
            self._width = width
        else:
            print("Error!\n")
            exit()

    def perimeter(self):
        print("The perimeter of a rectangle is:\n", 2 * (self._length + self._width))

    def area(self):
        print("The area of a rectangle is:\n", self._length * self._width)
