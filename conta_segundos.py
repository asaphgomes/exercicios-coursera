entrada = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dia = entrada // 86400
hora = (entrada % 86400) // 3600
minutos = (entrada % 3600) // 60
segundos = entrada % 60

print(f"{dia} dias, {hora} horas, {minutos} minutos e {segundos} segundos.")

#segundos = (entrada % 3600) % 60