import sys

from Cliente import Cliente
from Solicitud import Solicitud
from Simulacion import Simulacion

obj_cliente = Cliente()
obj_solicitud = Solicitud()
obj_simulacion = Simulacion()

obj_solicitud.monto = int(input("ingresa el monto: "))
obj_solicitud.cuotas = int(input("ingresa en numero de cuotas: "))

if obj_solicitud.monto <= 20000000:
    if 6 <= obj_solicitud.cuotas >= 12:
        interes = 21.1
        obj_simulacion.calcular_valores_credito(obj_solicitud.monto, obj_solicitud.cuotas, interes)

    elif 12 < obj_solicitud.cuotas > 25:
        interes = 25.5
        obj_simulacion.calcular_valores_credito(obj_solicitud.monto, obj_solicitud.cuotas, interes)

    elif 24 < obj_solicitud.cuotas < 49:
        interes = 29.9
        obj_simulacion.calcular_valores_credito(obj_solicitud.monto, obj_solicitud.cuotas, interes)

    else:
        print("solo se admite hasta 48 cuotas")


else:
    print("porfavor acercarte a una sucursal para tramitar ese monto")

print("el valor de cada cuota con interes es: " + str(obj_simulacion.cuota_con_interes))
print("el valor de cada cuota sin interes es: " + str(obj_simulacion.cuota_sin_interes))
print("el costo total del credito es: " + str(obj_simulacion.total))
print(("La tasa de interes apriclada es de: {}".format(interes)))
print("el valor de timbre y estampilla es: " + str(obj_simulacion.impuesto_te))
