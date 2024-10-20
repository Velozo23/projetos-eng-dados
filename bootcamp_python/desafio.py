#bonus_fixo = 1000

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



# lista_impar = []

# lista_par = []

# valores = [2, 5, 6, 4, 8, 9, 15, 78, 69, 77, 65, 66, 42, 63, 44, 30, 99, 8, 28, 24, 23, 47, 33]

# for i in valores:
#     if i%2 == 0:
#         lista_par.append(i)
#     else:
#         lista_impar.append(i)


# print(f"A lista de valores pares sao: {lista_par}")
# print(f"A lista de valores impares sao: {lista_impar}")


texto = '''arte de levar aproximadamente 28 minutos para decidir o que assistir na Netflix e então escolher uma opção que parece bacana e pensar "Tem algo familiar nesse filme, eu acho que eu já vi algum pedaço dele antes, mas eu devo ter dormido no meio porque não lembro do final".

E então assistir.


E então conseguir me manter acordada por todo o filme.


E então quando está quase no finalzinho perceber "Nossa, mas eu to acertando todas as coisas que acontecem nesse filme" e se sentir o máximo até cair a ficha que você não só já viu esse filme, como achou o final uma porcaria - e dá uma baita sensação de déjà vu do déjà vu, porque aí cai outra ficha que: não é somente a segunda vez que você já assistiu esse filme, mas é a SEGUNDA VEZ QUE VOCÊ ESQUECEU QUE JÁ VIU ESSE FILME E ASSISTE DE NOVO (essa última vez, na verdade, foi a terceira vez que eu vi) - ou seja, você não é o máximo.


Obs.: Infelizmente isso não é uma metáfora sobre nada na minha vida, é um situação real com um filme com final bem bobo e sem graça.


Obs. 2: Mas se pensar bem, até funciona como metáfora também.



[originalmente publicado em 11 de outubro de 2012 no meu extinto blog 

"Eu ainda estava morta...'''

palavras_sep = texto.split()

qtd_palavras = {}

for i in palavras_sep:
    if i in qtd_palavras:
        qtd_palavras[i] += 1
    else:
        qtd_palavras[i] = 1

print(qtd_palavras)