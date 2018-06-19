# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Digite o salário do funcionário\nR$ '))
print(salario)
print('O novo salário do funcionário com 15% de aumento é R$ {:.2f}'.format(salario * 1.15))