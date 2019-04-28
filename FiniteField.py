class FiniteField():
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.p != other.p:
                raise Exception("You cannot add numbers on different fields");
            return FiniteField((self.n + other.n) % self.p, self.p)
        if isinstance(other, int):
            return FiniteField((self.n + other) % self.p, self.p)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self.p != other.p:
                raise Exception("You cannot subtract numbers on different fields");
            return FiniteField((self.n - other.n) % self.p, self.p)
        if isinstance(other, int):
            return FiniteField((self.n - (other % self.p)) % self.p, self.p)
        
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            if self.p != other.p:
                raise Exception("You cannot multiply numbers on different fields");
            return FiniteField((self.n * other.n) % self.p, self.p)
        if isinstance(other, int):
            return FiniteField((self.n * other) % self.p, self.p)
        
    def __rmul__(self, other):
        return self.__mul__(other)

    def __realdiv__(self, other):
        return self.__floordiv__(other)
        
    def __floordiv__(self, other):
        if isinstance(other, self.__class__):
            if self.p != other.p:
                raise Exception("You cannot divide numbers on different fields");
            return FiniteField((self.n * self.inv(other.n)) % self.p, self.p)
        if isinstance(other, int):
            return FiniteField((self.n * (self.inv(other) % self.p)) % self.p, self.p)
        
    def __neg__(self):
        return FiniteField(-self.n, self.p)

    def __pow__(self, other):
        if isinstance(other, self.__class__):
            if self.p != other.p:
                raise Exception("You cannot divide numbers on different fields");
            return FiniteField((self.n ** other.n) % self.p, self.p)
        if isinstance(other, int):
            return FiniteField((self.n ** other) % self.p, self.p)

    def __str__(self):
        return str(self.n) + " in F_" + str(self.p)
        
    def inv(self, x):
        s = 0
        new_s = 1
        r = self.p
        new_r = x
        #when new_r == 1 we will have s = a^-1
        while new_r > 0:
            #find the quotient of r/new_r (integer division)
            q = r // new_r
            #find the new values for s and r
            (r, new_r) = (new_r, r - (q * new_r))
            (s, new_s) = (new_s, s - (q * new_s))
            
            #if r is greater than 1 then gcd(a, N) is not 1 and therefore
            #a and N are not coprime and so a^-1 doesn't exist
        if r > 1:
            raise Exception(str(x) + " does not have a modular inverse mod "
                            + str(self.p))
        else:
            #incase the s found is negative
            if s < 0:
                s = s + self.p
        return s
