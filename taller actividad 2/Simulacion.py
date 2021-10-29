class Simulacion:
    interes = None

    def calcular_valores_credito(self, monto, cuotas, interes):
        self.cuota_sin_interes= monto/cuotas
        self.interes_de_cuota= self.cuota_sin_interes * (interes / 100)
        self.cuota_con_interes= self.cuota_sin_interes+ self.interes_de_cuota
        self.valor_credito= self.cuota_con_interes * monto
        self.impuesto_te= self.valor_credito * 0.01
        self.total= self.valor_credito + self.impuesto_te





