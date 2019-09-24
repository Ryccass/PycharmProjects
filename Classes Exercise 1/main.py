class Triangle:
    numberOfSides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def checkAngles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


myTriangle = Triangle(90, 30, 60)
print(myTriangle.checkAngles())
print(myTriangle.numberOfSides)
