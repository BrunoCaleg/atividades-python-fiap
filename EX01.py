tipo_de_assinatura = input("Por favor, informe seu nivel de assinatura ").upper()
faturamento_anual = float(input("Por favor, informe seu faturamento anual "))

if tipo_de_assinatura == "BASIC":
    valor_final = faturamento_anual * 0.30
    print(f"O valor a ser pago sera de R${valor_final:.2f}, equivalente á 30% sobre faturamento para clientes Basic")
elif tipo_de_assinatura == "SILVER":
    valor_final = faturamento_anual * 0.20
    print(f"O valor a ser pago sera de R${valor_final:.2f}, equivalente á 20% sobre faturamento para clientes Silver")
elif tipo_de_assinatura == "GOLD":
    valor_final = faturamento_anual * 0.10
    print(f"O valor a ser pago sera de R${valor_final:.2f}, equivalente á 10% sobre faturamento para clientes Gold")
elif tipo_de_assinatura == "PLATINUM":
    valor_final = faturamento_anual * 0.05
    print(f"O valor a ser pago sera de R${valor_final:.2f}, equivalente á 5% sobre faturamento para clientes Platinum")
else:
    print("Sua assinatura é inválida")
