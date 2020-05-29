# Coursera Python Training 2
# Lucas Silva
# Week 3 - Exercício 1 - Perímetro de Triângulos - OBJ

class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c