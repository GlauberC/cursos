# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pegar, sabendo que o carro custa R$ 60 por dia e R$0,15 por km rodado.

custoCarro = 60
custoKm = .15
diasAlugados = int(input('Dias alugados: '))
print(diasAlugados)
kmPercorrido = float(input('KM percorrido: '))
print(kmPercorrido)
print('Diária R$ {:.2f}\nCusto por km {:.2f}\nTotal: R$ {:.2f}'.format(custoCarro, custoKm,
                                                             diasAlugados * custoCarro + kmPercorrido * custoKm))
