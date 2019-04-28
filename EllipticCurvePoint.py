class Point():
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve
        
    def copy(self):
        return Point(self.x, self.y, self.curve)

    def doIExist(self):
        return ((self.y**2)  ==
                (self.x**3 + self.x*self.curve.A + self.curve.B))
    
    #elliptic point addition
    def __add__(self, other):
        #check if either point is zero
        if self == self.curve.O:
            return other
        if other == self.curve.O:
            return self
        #check if the second point is a reflection in x
        if self.x == other.x and self.y == -other.y:
            return self.curve.O
        
        #if we are doubling
        if self == other:
            l_1 = 3 * self.x**2 + self.curve.A
            l_2 = 2 * self.y
            #if we are adding normally
        else:
            l_1 = other.y - self.y
            l_2 = other.x - self.x
            #if the denominator is 0: vertical line
        if l_2 == 0:
            return self.curve.O
        #find the slope
        l = l_1 / l_2

        #find the x,y co-ords of the new point
        x_3 = l**2 - self.x - other.x
        y_3 = l*(self.x - x_3)-self.y
        
        return Point(x_3, y_3, self.curve)

    #double-and-add algorithm
    def __mul__(self, n):
        if isinstance(n, self.__class__):
            raise Exception("Cannot multiply a point with a point")
        if isinstance(n, int):          
            P = self
            Q = P.copy()
            R = self.curve.O
            i = n
            while i > 0:
                if i % 2 == 1:
                    R = R + Q
                    Q = Q + Q
                    i = i//2
                    
            return R
        
    def __rmul__(self, n):
        return self.__mul__(n)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")" 
