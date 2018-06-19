# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

carteira = float(input('Quantos reais você tem na carteira? \nR$ '))
print(carteira)
print('Você tem R$ {:.2f} , com esse dinheiro você pode comprar US$ {:.2f}'.format(carteira, carteira/3.27))