aluno_par = 0
aluno_impar = 0

for alunos in range(2, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nota_par = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {alunos} "))
    aluno_par = aluno_par + nota_par
aluno_par = aluno_par / 25
print("***********************************************************")
for alunos2 in range(1, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    nota_impar = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {alunos2} "))
    aluno_impar = aluno_impar + nota_impar
aluno_impar = aluno_impar / 25
print("***********************************************************")
if aluno_par > aluno_impar:
    print(f"Alunos pares ficaram com a média de {aluno_par:.2f}, enquanto os alunos ímpares ficaram com média de "
          f"{aluno_impar:.2f}, logo os alunos pares possuem nota média maior.")
elif aluno_impar > aluno_par:
    print(f"Alunos pares ficaram com a média de {aluno_par:.2f}, enquanto os alunos ímpares ficaram com média de "
          f"{aluno_impar:.2f}, logo os alunos impares possuem nota média maior.")
else:
    print(f"A média dos alunos pares foi de {aluno_par:.2f}, enquanto os alunos ímpares ficaram com média "
          f"de {aluno_impar:.2f}, logo ocorreu um empate em ambas as médias. ")