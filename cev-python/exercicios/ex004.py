# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

entrada = input('Digite algo na tela: ')
print(entrada, '\n')
print('O tipo é {}\n'
      'Só tem espaços? {}\n'
      'É um número? {}\n'
      'É alfabético? {}\n'
      'É alfanumérico? {}\n'
      'Está em maiúscula? {}\n'
      'Está em minúscula? {}\n'
      'Está capitalizada? {}\n'.format(
        type(entrada),
        entrada.isspace(),
        entrada.isnumeric(),
        entrada.isalpha(),
        entrada.isalnum(),
        entrada.isupper(),
        entrada.islower(),
        entrada.istitle()))
