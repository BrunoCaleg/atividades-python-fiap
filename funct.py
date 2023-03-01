def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    return velocidade_media

def soma(distancia, tempo) :
        c = tempo + distancia
        return c

distancia = float(input("Informe a distância"))
tempo = float(input("Informe o tempo"))

calcularVelocidadeMedia(distancia, tempo)
print(f"A velocidade média é {calcularVelocidadeMedia(distancia, tempo)} km/h")
soma(distancia, tempo)
print(f"A soma é {soma(distancia, tempo)}")
