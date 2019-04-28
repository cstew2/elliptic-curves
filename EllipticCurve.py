class EllipticCurve():
    inf = -1
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.O = Point(EllipticCurve.inf, EllipticCurve.inf, self)

    def __str__(self):
        return "Y^2 = X^3 + " + str(self.A) + "X + " + str(self.B)
