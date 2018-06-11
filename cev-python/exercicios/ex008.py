# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor em metros: '))
print(m)
print('{:.2f} m => {:.2f} cm => {:.2f} mm'.format(m, m*100, m*1000.))
