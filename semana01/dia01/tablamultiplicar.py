#ENTRADA
tabla = input("Ingrese tabla de multiplicar: ")
#PROCESO
for contador in range(1,12,1):
    print(tabla + " x " +str(contador)+ " = " + str(contador*int(tabla)))