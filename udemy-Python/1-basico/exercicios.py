#Python 3.2
"""
1 - imprimir nome na tela
2 - pedir nome
3 - pedir nome e idade
4 e 5 - pedir numero
6 e 7 - soma
8 - Media
9 - conversao
10 - cubo e quadrado
11 - Divisao e inteiro
12 - Altura x Largura
13 - Conversao para segundos
14 - Valor do produto
"""

#1 - imprimir nome na tela

print("Glauber Carvalho")


#2 - pedir nome

nome = input("Digite seu none: ")
print("O seu nome eh ", nome)

#3 - pedir nome e idade

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print("O seu nome eh %s e sua idade eh %s" %(nome, idade))

#4 e 5 - pedir numero

num = float(input("Digite um numero: "))
print("O numero digitado foi:" ,num)

#6 e 7 - soma

num_1 = float(input("Digite o primeiro numero: "))
num_2 = float(input("Digite o segundo numero: "))
num_3 = float(input("Digite o terceiro numero: "))
soma = num_1 + num_2 + num_3
print("A soma foi: ", soma)

#8 - Media

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota "))
nota_4 = float(input("Digite a quarta nota "))
media = (nota_1 + nota_2 + nota_3 + nota_4)/4
print("A media foi: ",media)


#9 - conversao

metros = float(input("Digite um valor em metros: "))
centimetros = metros*100.0
print("%.2f centimetros" %centimetros)


#10 - cubo e quadrado

num = float(input("Digite um numero: "))
print("Quadrado: %.2f \nCubo: %.2f" %(num**2, num**3))


#11 - Divisao e inteiro

num_1 = float(input("Digite um numero: "))
num_2 = float(input("Digite outro numero: "))
print("Divisao: %f \nInteiro: %i" %(num_1/num_2, num_1//num_2))


#12 - Altura x Largura

altura = float(input("Digite a altura: "))
largura = float(input("Digite a largura: "))
print("Esse retangulo possui %.2f metros quadrados" %(altura*largura))


#13 - Conversao para segundos

dias = int(input("Digite o numero exato de dias: "))
horas = int(input("Digite o numero exato de horas: "))
minutos = int(input("Digite o numero exato de minutos: "))
segundos = int(input("Digite o numero exato de segundos: "))
horas = horas + dias * 24
minutos = minutos + horas * 60
segundos = segundos + minutos * 60
print("O numero total de segundos eh: ", segundos)


#14 - Valor do produto

valor = float(input("Digite o valor do produto: R$ "))
valor_do_desconto = valor * 0.1
valor_com_desconto = valor - valor_do_desconto
print("O produto tera um desconto de R$ %.2f totalizando R$ %.2f " %(valor_do_desconto, valor_com_desconto))







