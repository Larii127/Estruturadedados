
class Circulo:

    def __init__(self, raio):
        self.raio = raio

    def caucular_area(self):
        area = 3.14 * self.raio
        return area

circulo1 = Circulo(7)
print(circulo1.caucular_area())


