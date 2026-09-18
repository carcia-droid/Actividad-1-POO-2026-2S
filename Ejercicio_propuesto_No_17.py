import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0
        self.longitud = 0

    def calcular_area(self):
        self.area = math.pi * self.radio ** 2

    def calcular_longitud(self):
        self.longitud = 2 * math.pi * self.radio

    def mostrar_resultados(self):
        print(f"Área del círculo: {self.area:.2f}")
        print(f"Longitud de la circunferencia: {self.longitud:.2f}")


radio = float(input("Ingrese el radio del círculo: "))

circulo = Circulo(radio)
circulo.calcular_area()
circulo.calcular_longitud()
circulo.mostrar_resultados()
