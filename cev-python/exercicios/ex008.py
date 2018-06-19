# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor em metros: '))
print(m)
print('{:.4f}km\n{:.2f}hm\n{:.2f}dam\n{:.2f}m\n{:.2f}dm\n{:.2f}cm\n{:.2f}mm'.format(m / 1000, m / 100, m / 10, m,
                                                                                    m * 10, m * 100, m * 1000))
