#Python 3.2
"""
Operacoes basicas
Modulo da divisao
Exemplo
Potenciacao e radiacao
Importar math
Operadores relacionais
"""

#operacoes basicas
num1 = 4
num2 = 2

soma = 4 + 2
subtracao = 4 - 2
divisao = 4 / 2
multiplicacao = 4 * 2
expressao = (10 +2) * 4
resultado_inteiro = 10//3

print("Soma:", soma)
print("Subtracao:", subtracao)
print("Divisao:", divisao)
print("Multiplicacao:", multiplicacao)
print("Expressao:", expressao)
print("Resultado inteiro:", resultado_inteiro)

#Modulo da divisao
modulo1_div = 2%2
modulo2_div = 3%2
print("\nModulo da divisao: %i e %i" %(modulo1_div, modulo2_div))


#exemplo
"""
print("Exemplo de divisao")
num_a = float(input("Digite um numero: "))
num_b = float(input("Digite outro numero: "))
resultado = num_a / num_b
resto = num_a % num_b
print("O resultado da divisao de %f com %f eh: %.2f"%(num_a, num_b, resultado))
print("O resto da divisao eh:", resto)
"""

#Potenciacao e radiacao
num_pot = 5**2
print("\nPotenciacao:", num_pot)
num_rad = 8**(1/3)
print("Potenciacao:", num_rad)

#importar math
import math
dir_math = dir(math)
print()
print(dir_math)
print(math.pi)

#Operadores relacionais
op_igual = 4==4
op_dif = 4!=3
op_maior = 4>6
op_menor = 4<3
op_maior_igual = 4>=4
op_menor_igual = 3<=3

print("\nOperador de igualidade(4 ==4 ?): ",op_igual)
print("Operador diferenca (4 != 3?): ",op_dif)
print("Operador maior (4 > 6?): ",op_maior)
print("Operador menor (4 < 3?): ",op_menor)
print("Operador maior igual (4 >= 4?): ",op_maior_igual)
print("Operador menor igual (3 <= 3?): ",op_menor_igual)





