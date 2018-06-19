# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input('Digite um ângulo qualquer: '))
print(ang)
angRad = math.radians(ang)
print(angRad)

print('sen({:.2f}) = {:.2f}'.format(ang, math.sin(angRad)))
print('cos({:.2f}) = {:.2f}'.format(ang, math.cos(angRad)))
print('tan({:.2f}) = {:.2f}'.format(ang, math.tan(angRad)))
