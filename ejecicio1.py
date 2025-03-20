N = 0
temperaturas = []
suma = 0
media = 0
c = 0

N = int(input("Ingrese la cantidad de temperaturas: "))
for i in range(0,N):
    temperatura = float(input("Ingrese la temperatura: "))
    temperaturas.append(temperatura)  
    suma += temperatura  # Sumar la temperatura actual

media = suma / N 


for temperatura in temperaturas:
    if temperatura >= media:
        c += 1

# Mostrar los resultados
print("Media:", round(media, 2))
print("Mayores o iguales a la media:", c)


        

