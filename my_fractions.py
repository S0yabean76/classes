from fractions import Fraction

class MyFraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
        gcd(self.num, self.den)

    def __repr__(self):
        return '%s/%s' % (self.num, self.den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __div__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __eq__(self, other):
        return (self.num * self.den) == (other.num * other.den)

    def __ne__(self, other):
        return (self.num * self.den) != (other.num * other.den)

    def __lt__(self, other):
        return float(self.num) / self.den < float(other.num) / other.den

    def __gt__(self, other):
        return float(self.num) / self.den > float(other.num) / other.den



f1 = Fraction(1,2)
f2 = Fraction(1,2)
f3 = Fraction(1,2)
f4 = f1 + f2 + f3

print f4

