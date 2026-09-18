class OperacionesNumero:
    def __init__(self, numero):
        self.numero = numero
        self.cuadrado = 0
        self.cubo = 0

    def calcular(self):
        self.cuadrado = self.numero ** 2
        self.cubo = self.numero ** 3

    def mostrar_resultados(self):
        print(f"Cuadrado: {self.cuadrado}")
        print(f"Cubo: {self.cubo}")


numero = float(input("Ingrese un número: "))

operacion = OperacionesNumero(numero)
operacion.calcular()
operacion.mostrar_resultados()
