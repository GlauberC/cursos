#Python 3.2
"""
selecao unica
senao
elif
exemplo
exemplo 2
operadores logicos
"""


#selecao unica
num = 10
if(num == 10):
    print("Esse numero eh igual a 10")

#senao
idade = int(input("Digite a idade: "))
if(idade >= 18):
    print("Maior de idade")
else:
    print("Menor de idade")


#elif
decisao = int(input("Digite '1' para dizer que sim e '2' para dizer que nao: "))

if(decisao == 1):
    print("SIM")
elif(decisao == 2):
    print("NAO")
else:
    print("Era para digitar apenas 1 ou 2")


#exemplo
idade = int(input("Digite a sua idade: "))
if(idade<=0):
    print("Sua idade nao pode ser 0 ou negativa")
elif(idade>=150):
    print("Voce nao pode ter mais de 150 anos")
elif(idade < 18):
    print("Voce precisa ser maior que 18 anos")
else:
    print("Voce eh maior que 18 anos")

#exemplo 2
num_1 = int(input("Digite o primeiro numero: "))
num_2 = int(input("Digite o segundo numero: "))
if(num_1 == num_2):
    print("O numero %i eh igual a %i" %(num_1, num_2))
else:
    print("O numero %i eh diferente de %i" %(num_1, num_2))
    if(num_1 > num_2):
        print("O numero %i eh maior que %i" %(num_1, num_2))
    else:
        print("O numero %i eh menor que %i" %(num_1, num_2))


#operadores logicos
print("operadores logicos")
caso_1 = 4>3 and 2<3
caso_2 = 4>3 or 2>3
caso_3 = not(3<4)
caso_4 = 4 is 4
caso_5 = 4 is not 4
caso_6 = 3 in {3,4}
caso_7 = 3 not in {3,4}

print("4>3 and 2<3?", caso_1)
print("4>3 or 2>3?", caso_2)
print("not(3<4)?", caso_3)
print("4 is 4?", caso_4)
print("4 is not 4?", caso_5)
print("3 in {3,4}?", caso_6)
print("3 not in {3,4}?", caso_7)



