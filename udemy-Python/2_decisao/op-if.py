#Python 3.2
"""
selecao unica
senao
elif

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


