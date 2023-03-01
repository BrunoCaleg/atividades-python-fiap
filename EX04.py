minuto = int(input("Qual minuto o computador esta marcando em seu relógio ? "))
inicio = 1
for n in range(1, minuto+1):
    inicio *= n
if minuto > 59:
    print("Esse minuto é inexistente. ")
else:
    print(f"A senha é LIBERDADE{inicio}")
