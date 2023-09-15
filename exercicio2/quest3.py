class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def caucular_area(self):
        area = self.base * self.altura
        return area

retangulo1 = Retangulo(7,7)
print(retangulo1.caucular_area())