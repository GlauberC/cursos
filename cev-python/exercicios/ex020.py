# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

nome1 = input('Digite o nome do primeiro aluno: ')
print(nome1)
nome2 = input('Digite o nome do segundo aluno: ')
print(nome2)
nome3 = input('Digite o nome do terceiro aluno: ')
print(nome3)
nome4 = input('Digite o nome do quarto aluno: ')
print(nome4)

ordem = [nome1, nome2, nome3, nome4]
random.shuffle(ordem)
print('A ordem de apresentação será: {}'.format(ordem))