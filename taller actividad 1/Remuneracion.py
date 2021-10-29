class Remuneracion:
    valor_hora = None
    horas_trabajadas = None
    pago = None
    incremento = 1.5

    def calcular_pago_normal(self, valor_hora, horas_trabajadas):
        self.pago = valor_hora * horas_trabajadas

    def calcular_extra(self,horas_trabajadas, valor_hora, incremento):
        self.extra = (((horas_trabajadas - 40) * valor_hora) * incremento)

    def calcular_liquido(self, sueldo, extra, descuento):
        self.liquido: sueldo + extra - descuento
