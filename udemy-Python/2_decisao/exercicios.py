#Python 3.2


#1 - Positivo negativo ou zero
num = int(input("Digite um numero: "))
if(num > 0):
    print("Positivo")
elif(num < 0):
    print("Negativo")
else:
    print("Zero")

#2 e 7 - Par ou impar
num = int(input("Digite um numero: "))
if(num%2 == 0):
    print("par")
else:
    print("impar")

#3 - imprime o maior
num_1 = int(input("Digite o primeiro numero: "))
num_2 = int(input("Digite o segundo numero: "))
if(num_1 > num_2):
    print(num_1 ," eh maior")
else:
    print(num_2 ," eh maior")

#4 - maior de idade
idade = int(input("Digite a idade: "))
if(idade<18):
    print("Menor de idade")
else:
    print("Maior de idade")

#5 - idade da mae no nascimento
idade_filho = int(input("Digite a idade do filho: "))
idade_mae = int(input("Digite a idade da mae: "))
idade_no_nascimento = idade_mae - idade_filho
print("A mae teve o filho com %s anos" %idade_no_nascimento)

#6 - imrpimir 50x -
print(50*'-')


#8 - imprimir maior e depois o menor
num_1 = int(input("Digite o primeiro numero: "))
num_2 = int(input("Digite o segundo numero: "))
if(num_1 > num_2):
    print(num_1)
    print(num_2)
else:
    print(num_2)
    print(num_1)


#9 - Verifica se o numero eh inteiro
num = int(input("Digite um numero: "))
if(type(num) is int):
    print("O numero %i eh inteiro"%num)

#10 - Verifica String
string_var = input("Digite uma string: ")
if(type(string_var) is str):
    print("A variavel %s eh uma string"%string_var)
    
#11 - Verifica Decimal
decimal = float(input("Digite um numero decimal: "))
if(type(decimal) is float):
    print("O numero %f eh decimal"%decimal)


#12 - Inteiro ou decimal
num = input("Digite um numero inteiro ou decimal: ")
if('.' in num):
    print("O numero %s eh decimal"%num)
else:
    print("O numero %s eh inteiro"%num)

#13 - O maior entre 3
num_1 = float(input("Digite o primeiro numero: "))
num_2 = float(input("Digite o segundo numero: "))
num_3 = float(input("Digite o terceiro numero: "))
maior = num_1
if(num_1<num_2):
    maior = num_2
if(maior<num_3):
    maior = num_3
print("O maior numero eh: ", maior)

#14 - Ordem crescente
num_1 = float(input("Digite o primeiro numero: "))
num_2 = float(input("Digite o segundo numero: "))
num_3 = float(input("Digite o terceiro numero: "))
primeiro = num_1
segundo = num_2
terceiro = num_3
if(num_1 > num_2):
    primeiro = num_2
    segundo = num_1
if(segundo > num_3):
    terceiro = segundo
    segundo = num_3
if(primeiro > segundo):
    temp = primeiro
    primeiro = segundo
    segundo = temp
print("%f > %f > %f"%(primeiro, segundo, terceiro))


#15 - eh vogal
char_var = input("Digite um char: ")
if(char_var in "aeiouAEIOU"):
    print("%s eh uma vogal"%char_var)
else:
    print("%s nao eh uma vogal"%char_var)


#16 - Verifica ip
ip = input("Digite um ip: ") #ex: 168.192.0.1
if('.' in ip[0:3] or float(ip[0:3]) <= 127):
    print("Esse IP eh classe A")
elif(int(ip[0:3]) <= 191):
    print("Esse IP eh classe B")
elif(int(ip[0:3]) <= 223):
    print("Esse IP eh classe C")
elif(int(ip[0:3]) <= 239):
    print("Esse IP eh classe D")
else:
    print("Esse IP eh classe E")



#17 - Numero mes
num_mes = int(input("Digite o numero do mes: "))
mes = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
if(num_mes <=0 or num_mes >12):
    print("O numero nao corresponde a um mes")
else:
    print(mes[num_mes - 1])

#18 - Valida data
validar = True
numero = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
mes_31 = ["01", "03", "05", "07", "08", "10", "12"]
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia = data[0:2]
mes = data[3:5]

    #validacao de estrutura
if(data[0] not in numero or data[1] not in numero):
    validar = False
    print("O dia precisa estar no padrao dd/")
    
elif(data[2] != '/'):
    validar = False
    print("Apos o dia (dd) nao foi encontrado a /")
    
elif(data[3] not in numero or data[4] not in numero):
    validar = False
    print("O mes precisa estar no padrao mm/")
    
elif(data[5] != '/'):
    validar = False
    print("Apos o mes (mm) nao foi encontrado a /")
    
elif(data[6] not in numero or data[7] not in numero or data[8] not in numero or data[9] not in numero):
    validar = False
    print("O ano precisa estar no padrao aaaa")

    #validacao de valor
if(dia == "00"):
    validar = False
    print("Nao existe o dia 00")
    
elif(int(dia) > 31):
    validar = False
    print("O dia eh inexistente")
    
elif(mes == "02" and int(dia)>29):
    validar = False
    print("Nesse mes nao ha esse dia")
    
elif(mes == "00" or int(mes) > 12):
    validar = False
    print("Nao existe esse mes")
    
elif(mes not in mes_31):
    if(int(data[0:2]) > 30):
        validar = False
        print("Nesse mes nao ha esse dia")




    

