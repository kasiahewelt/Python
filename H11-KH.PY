
class ComplexNumbers:
    def __init__(self,real = 0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return"{} {} {}i".format(self.real, "+" if self.imag >= 0 else 0, abs(self.imag))

    def __add__(self, other):
        return ComplexNumbers(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return ComplexNumbers(self.real - other.real, self.imag - other.imag)
    
    def __abs__(self):
        return ((self.real**2 + self.imag**2))**(1/2)

a = ComplexNumbers(1,4)
b = ComplexNumbers(3,6)
c = ComplexNumbers(5)
d = ComplexNumbers(2)
print(a)
print(b)
print(a+b)
print(b-a)
print(abs(a))
print(c)
print(d)
print(c-d)