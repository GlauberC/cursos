# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa


import math
# from math import sqrt, pow

co = float(input('Digite o tamanho do cateto oposto: '))
print(co)
ca = float(input('Digite o tamanho do cateto adjacente: '))
print(ca)

# hi = sqrt(pow(co, 2)+pow(ca, 2))

hi = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hi))