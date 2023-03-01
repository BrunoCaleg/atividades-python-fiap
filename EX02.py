nvotos = int(input("Por favor, digite o número de alunos que irão votar "))

A = 0
B = 0
C = 0
D = 0
E = 0

for voto in range(0, nvotos):
    qvoto = input("Digite a letra correspondente ao dia da semana que você considere o melhor para a realização das"
                  " lives: \n (A) - Segunda-feira, (B) - Terça-feira, (C) - Quarta-feira, (D)- Quinta-feira ou (E) - "
                  "Sexta-feira ? ").upper()
    if qvoto == "A":
        A = A + 1
    elif qvoto == "B":
        B = B + 1
    elif qvoto == "C":
        C = C + 1
    elif qvoto == "D":
        D = D + 1
    elif qvoto == "E":
        E = E + 1
    else:
        print("Voto inválido")
print("*************************")
if A > B and A > C and A > D and A > E:
    print("Segunda-feira venceu")
elif B > A and B > C and B > D and B > E:
    print("Terça-feira venceu")
elif C > A and C > B and C > D and C > E:
    print("Quarta-feira venceu")
elif D > A and D > B and D > C and D > E:
    print("Quinta-feira venceu")
elif E > A and E > B and E > C and E > D:
    print("Sexta-feira venceu")
elif qvoto != "A" and qvoto != "B" and qvoto != "C" and qvoto != "D" and qvoto != "E":
    print("Votação invalidada")
else:
    print("Houve empate, necessária uma nova votação")
