class EdadesFamilia:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan
        self.edad_alberto = 0
        self.edad_ana = 0
        self.edad_mama = 0

    def calcular_edades(self):
        self.edad_alberto = (2 / 3) * self.edad_juan
        self.edad_ana = (4 / 3) * self.edad_juan
        self.edad_mama = (
            self.edad_juan
            + self.edad_alberto
            + self.edad_ana
        )

    def mostrar_resultados(self):
        print(f"Edad de Juan: {self.edad_juan:.2f} años")
        print(f"Edad de Alberto: {self.edad_alberto:.2f} años")
        print(f"Edad de Ana: {self.edad_ana:.2f} años")
        print(f"Edad de la mamá: {self.edad_mama:.2f} años")


edad_juan = float(input("Ingrese la edad de Juan: "))

familia = EdadesFamilia(edad_juan)
familia.calcular_edades()
familia.mostrar_resultados()
