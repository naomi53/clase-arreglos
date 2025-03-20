cantidad = int(input("ingresa los valores"))
vectores = []
vectoresSinRepetir = []

for i in range(0, cantidad):
    if 5 < cantidad < 200:
        valores = float(input(f"Ingrese los valores:{i +1} "))
        vectores.append(valores)
        vectoresSinRepetir = list(set(vectores))
        vectoresSinRepetir.sort()

        print("Vecotres repetidos",vectores)
        print("vectores sin repetir", vectoresSinRepetir)
    else:
        print("no hay datos suficientes para para el procesamineto")
