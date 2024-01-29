#Programa para calcular la distancia recorrida en un movimiento rectilíneo. Recuerde $x=v*t$ donde $v$ es velocidad y $t$ es tiempo. 
#Solicitar al usuario velocidad en kilómetros por hora (Km/h) y tiempo en horas (h) para obtener la distancia en kilómetros (Km).
velocidad = float(input("Ingrese la velocidad en Km/h: "))
tiempo = float(input("Ingrese el tiempo en horas: "))
distancia = velocidad * tiempo
print("La distancia recorrida es:", distancia, "Km")
