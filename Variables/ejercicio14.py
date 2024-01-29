#Solicitar al usuario una distancia en metros y transformar a km., cm. o mm. 
metros = float(input("Ingrese la distancia en metros: "))
distancia_km = metros / 1000
distancia_cm = metros * 100
distancia_mm = metros * 1000
print("La distancia en Km es:", distancia_km)
print("La distancia en cm es:", distancia_cm) 
print("La distancia en mm es:", distancia_mm)
