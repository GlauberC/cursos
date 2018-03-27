#Python 3.2
"""
Operacoes basicas
Modulo da divisao
Exemplo
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
print("Modulo da divisao: %i e %i" %(modulo1_div, modulo2_div))

#exemplo
print("Exemplo de divisao")
num_a = float(input("Digite um numero: "))
num_b = float(input("Digite outro numero: "))
resultado = num_a / num_b
resto = num_a % num_b

print("O resultado da divisao de %f com %f eh: %.2f"%(num_a, num_b, resultado))
print("O resto da divisao eh:", resto)
