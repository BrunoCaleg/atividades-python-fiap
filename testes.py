#exemplo de listas
n = []
cont = -1
while cont != 4:
    print(" 1 - INFORMAR NOTA \n 2 - EXIBIR NOTAS \n 3 - CALCULAR MÉDIA \n 4 - FECHAR PROGRAMA ")
    cont = int(input("\n Escolha a opção \n "))
    if cont==1:
        n.append(float(input("Digite a nota ")))
    elif cont==2:
        for x in n:
            print(x)
    elif cont==3:
        print(sum(n)/len(n))
#---------------------------------------------------------


