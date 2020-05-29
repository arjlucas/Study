# Coursera Python Training 2
# Lucas Silva
# Week 3 - Exercício Extra 2 - Triângulos Semelhantes

class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.lados=[self.a, self.b, self.c]
        
    def perimetro(self):
        return self.a + self.b + self.c
    
    def retangulo(self):
        self.lados.sort()
        if (pow(self.lados[0],2) == self.lados[1] + self.lados[2]):
            return True
        else:
            return False
        
    def tipo_lado(self):
        if (self.a==self.b and self.b==self.c):
            return 'equilátero'
        elif (self.a==self.b) or (self.a==self.c) or (self.c==self.b):
            return 'isósceles'
        else:
            return 'escaleno'
        
    def semelhantes(self, Triangulo):
        if (self.tipo_lado()) == (Triangulo.tipo_lado()):
            return True
        else:
            return False