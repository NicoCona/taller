from Trabajador import Trabajador
from Remuneracion import Remuneracion
from Honorarios  import Honorarios

obj_trabajador = Trabajador()
obj_remuneracion = Remuneracion()
obj_honorarios = Honorarios()

obj_trabajador.nombres= input("Ingresa los nombres: ")
obj_trabajador.apellidos= input("Ingresa los apellidos: ")
obj_trabajador.rut= input("Ingresa el rut: ")

obj_remuneracion.valor_hora = int(input("Ingrese en valor por hora: "))
obj_remuneracion.horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

if obj_remuneracion.horas_trabajadas < 41:
    obj_remuneracion.calcular_pago_normal(obj_remuneracion.horas_trabajadas, obj_remuneracion.valor_hora)



obj_remuneracion.calcular_pago_normal(obj_remuneracion.horas_trabajadas, obj_remuneracion.valor_hora)
obj_remuneracion.calcular_extra(obj_remuneracion.horas_trabajadas, obj_remuneracion.valor_hora, obj_remuneracion.incremento)
obj_honorarios.calcular_retencion(obj_remuneracion.pago, obj_honorarios.descuento)

print(str(obj_trabajador.nombres))
print(str(obj_trabajador.apellidos))
print(str(obj_trabajador.rut))
print("El pago extra es: {}" .format(obj_remuneracion.extra))
print("El pago normal es: " + str(obj_remuneracion.pago))
print("el desuento tiene el monto de: " + str(obj_honorarios.retencion))




