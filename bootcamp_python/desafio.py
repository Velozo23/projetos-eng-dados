bonus_fixo = 1000

# Informa o nome do usuario
#nome_usuario = input("Digite seu nome: ")

#if nome_usuario.isdigit():
#    print("Você digitou seu nome errado.")
#    exit()
#elif len(nome_usuario) == 0:
#    print("Você não digitou nada")
#    exit()
#elif nome_usuario.isspace():
#    print("Você apenas digitou espaço")
#    exit()

# Informa o valor do salario do usuario
#salario_usuario = float(input("Digite o seu salario: "))

# Informa qual o valor do bonus do usuario
#bonus_usuario = float(input("Digite o seu bonus: "))

# Calcula o valor do bonus do usuario
#valor_do_bonus = bonus_fixo + salario_usuario * bonus_usuario

# Imprime uma mensagem personalizada, incluindo o nome do usuario e o bonus dele.
#print(f"O usuario {nome_usuario} possui bonus de {valor_do_bonus}")



### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.


# idade_valida = []

# email_valido = []


# try:
#     idade = int(input("Informe sua idade: "))
#     #for i in idade:
#     if idade >= 18 and idade <= 65:
#         idade_valida = idade
#         print("Siga para a proxima etapa")
#     else:
#         print("informe uma idade valida, entre de 18 e 65 anos")

# except:
#     print("informe uma idade valida, entre de 18 e 65 anos")

# try:
#     email = input("Informe seu e-mail: ")

#     if email.endswith(".com.br"):
#         email_valido = email
#         print("O seu email foi salvo com sucesso")
#         print(f"As idades validas sao: {idade_valida}")
#         print(f"Os e-mails validos sao: {email_valido}")
#     else:
#         print("Informe um e-mail valido")
# except: 
#     print("Informe um e-mail valido")



lista_impar = []

lista_par = []

valores = [2, 5, 6, 4, 8, 9, 15, 78, 69, 77, 65, 66, 42, 63, 44, 30, 99, 8, 28, 24, 23, 47, 33]

for i in valores:
    if i%2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)


print(f"A lista de valores pares sao: {lista_par}")
print(f"A lista de valores pares sao: {lista_impar}")
