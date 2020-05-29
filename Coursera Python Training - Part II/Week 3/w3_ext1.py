# Coursera Python Training 2
# Lucas Silva
# Week 3 - Exercício Extra 1 - Triângulos Retângulos

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