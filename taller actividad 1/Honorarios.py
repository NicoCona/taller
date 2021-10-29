class Honorarios:
    descuento = 0.115

    def calcular_retencion(self, pago, descuento):
        self.retencion = pago * descuento
