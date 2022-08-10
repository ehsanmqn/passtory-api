from enum import Enum


# Standard photographic print size. Called "13 x 18 cm" worldwide.
class Paper_4R(Enum):
    height = 4
    width = 6
    padding = 50

    def __str__(self):
        return str(self.height) + " x " + str(self.width)

    def getSizePixel(self):
        return self.height * 300, self.width * 300, self.padding


# Standard photographic print size. Called "13 x 18 cm" worldwide.
class Paper_5R(Enum):
    height = 5
    width = 7
    padding = 50

    def __str__(self):
        return str(self.height) + " x " + str(self.width)

    def getSizePixel(self):
        return self.height * 300, self.width * 300, self.padding


class Paper_6R(Enum):
    height = 6
    width = 8
    padding = 50

    def __str__(self):
        return str(self.height) + " x " + str(self.width)

    def getSizePixel(self):
        return self.height * 300, self.width * 300, self.padding


# Standard photographic print size. Called "20 x 25 cm" worldwide.
class Paper_8R(Enum):
    height = 8
    width = 10
    padding = 50

    def __str__(self):
        return str(self.height) + " x " + str(self.width)

    def getSizePixel(self):
        return self.height * 300, self.width * 300, self.padding


# Standard photographic print size. Called "20 x 30 cm" worldwide.
class Paper_SBR(Enum):
    height = 8
    width = 12
    padding = 50

    def __str__(self):
        return str(self.height) + " x " + str(self.width)

    def getSizePixel(self):
        return self.height * 300, self.width * 300, self.padding