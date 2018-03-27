#Python 3.2
"""
valor
string
float
type
concatenar print
decimal no print
string no print
"""

#valor
num1_int = 10
num2_int = 2
print(num1_int + num2_int)
num2_int = 4
print(num1_int + num2_int)

#string
texto_str = "todo texto eh uma string"
print(texto_str)

#float
num_float = 2.4 + num1_int
print (num_float)

#saber o tipo
ty_texto = type(texto_str)
ty_num1 = type(num1_int)
ty_float = type(num_float)

print(ty_texto, ty_num1, ty_float)
"""
Toda variavel possui
    nome
    tipo
    tamanho
    valor
"""
#OBS - O TIPO DA VARIAVEL EH O PRIMEIRO ATRIBUIDO

#concatenar print
print("o numero escolhido eh.", num1_int)   #forma 1 - Virgula
print("o numero escolhido eh. %i" %num1_int)   #forma 2 - Tipo com % sem virgula
print("o numero escolhido eh. " +  str(num1_int))   #forma 3 - cast e concatenacao

#decimal no print
print("o decimal eh. %f" %num_float)
print("o decimal eh. %.2f" %num_float) #controle de casas decimais

#string no print
print("concatenando strings -", texto_str)
print("concatenando strings - %s" %texto_str)
print("concatenando strings - " + texto_str)
