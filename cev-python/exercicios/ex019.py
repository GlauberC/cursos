# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome do escolhido

import random

nome1 = input('Digite o nome do primeiro aluno: ')
print(nome1)
nome2 = input('Digite o nome do segundo aluno: ')
print(nome2)
nome3 = input('Digite o nome do terceiro aluno: ')
print(nome3)
nome4 = input('Digite o nome do quarto aluno: ')
print(nome4)

print('O aluno escolhido para limpar o quadro foi: {}'.format(random.choice([nome1, nome2, nome3, nome4])))