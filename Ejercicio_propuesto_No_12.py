class SalarioEmpleado:
    def __init__(self, horas_trabajadas, valor_hora, porcentaje_retencion):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0

    def calcular_salario(self):
        self.salario_bruto = self.horas_trabajadas * self.valor_hora
        self.retencion = self.salario_bruto * self.porcentaje_retencion
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar_resultados(self):
        print(f"Salario bruto: ${self.salario_bruto:,.0f}")
        print(f"Retención: ${self.retencion:,.0f}")
        print(f"Salario neto: ${self.salario_neto:,.0f}")


horas = 48
valor_hora = 5000
porcentaje_retencion = 0.125

empleado = SalarioEmpleado(
    horas,
    valor_hora,
    porcentaje_retencion
)

empleado.calcular_salario()
empleado.mostrar_resultados()
