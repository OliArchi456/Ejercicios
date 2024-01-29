#Solicitar tiempo en segundos y transformar a horas y minutos. 
segundos = int(input("Ingrese el tiempo en segundos: "))
horas = segundos // 3600
minutos = segundos // 60
print("El tiempo es:", horas, "horas y", minutos, "minutos")
