caracteres = int(input(f"Ingrese la cantidad de caracteres que tengra el vector:"))
arreglo = []

for i in range(0, caracteres):
    datos = str(input(f"Ingrese los datos: {i + 1}"))
    arreglo.append(datos)
    arreglo.sort(reverse=True)
    print("LOS DATOS REVERTIDOS", arreglo)
