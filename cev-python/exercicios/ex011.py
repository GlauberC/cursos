# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

larg = float(input('Digite a largura da parede: '))
print(larg)
alt = float(input('Digite a altura da parede: '))
print(alt)
area = alt * larg
metpergal = 2
print('A área da parede é {:.2f} m², portando é necessario {} galões de tinta'.format(area, area//metpergal + 1))
# Se o resultado for exato ele ainda assim adiciona + 1
