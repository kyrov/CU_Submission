class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary, self.real * no.imaginary + self.imaginary * no.real)
    def __truediv__(self, no):
        return Complex((self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2), (self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2))
    def __str__(self):
        if(self.imaginary == 0):
            return str(self.real)
        else:
            if(self.real == 0):
                if(self.imaginary == 1):
                    return "i"
                elif(self.imaginary == -1):
                    return "-i"
                else:
                    return str(self.imaginary) + "i"
            else:
                if(self.imaginary > 0):
                    if(self.imaginary == 1):
                        return str(self.real) + "+i"
                    else:
                        return str(self.real) + "+" + str(self.imaginary) + "i"
                else:
                    if(self.imaginary == -1):
                        return str(self.real) + "-i"
                    else:
                        return str(self.real) + "-" + str(abs(self.imaginary)) + "i"

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1+c2)
elif t == 4:
    print(c1*c2)
else:
    print(c1/c2)