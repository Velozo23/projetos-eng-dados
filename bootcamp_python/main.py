'''x = 2

if x < 0:
    x = 0
    print('`Negative change to zero')
elif x == 0:
    print('0')
elif x == 1:
    print('1')
elif x == 2:
    print('Voce chegou onde queria')
else:
    print('More')'''


'''quantidade = int(input('informe a quantidade de produtos de um item: '))
preço = float(input('Informe o valor do produto: '))  

if quantidade > 0 and preço > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")'''

lista_lobby = ["Marcos", "Leonardo", "Duarte", "Cheeng Choong", "Velozo"]

# Utilizando o for para percorrer todos os nomes pertencentes a lista do lobby
for i in lista_lobby:
    print("O jogador da rodada e: ", i)