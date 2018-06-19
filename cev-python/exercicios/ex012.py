# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço\nR$ '))
print(preco)
print('Com 5% de descento o novo preço é R& {:.2f}'.format(preco*0.95))