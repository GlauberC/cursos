# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
print('{}\n'.format(n))
print('Dobro:', 2 * n)
print('Triplo:', 3 * n)
print('Raiz quadrada: {:.2f}'.format(n ** (1 / 2)))
#print('Raiz quadrada: {:.2f}'.format(pow(n, 1/2))) # SEGUNDA FORMA
