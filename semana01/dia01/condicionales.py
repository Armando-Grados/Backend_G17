#ENTRADA

numero1 = input("Ingresa el numero1: ")
numero2 = input("Ingreso el numero2: ")
operacion = input("Operacion a ejecutar (sumar o restar): ")
#PROCESO

if(operacion == "sumar"):
  resultado = int(numero1) + int(numero2)
elif(operacion == "restar"):
  resultado = int(numero1) - int(numero2)
else:
  resultado = "nn"

#SALIDA
if(resultado == "nn"):
  print("Debe ingresar una operacion valida")
else:
  print("El resultado es: "+str(resultado))