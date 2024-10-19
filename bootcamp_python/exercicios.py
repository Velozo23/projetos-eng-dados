import math

# Escreva um programa que soma 2 numeros inteiros inseridos pelo usuário.

# Recebe um numero digitado pelo usuário.
#n1 = int(input("Digite um numero: "))

# Recebe outro numero digitado pelo usuário.
#n2 = int(input("Digite outro numero: "))
#Realiza o calculo da operação
#resultado = n1 // n2 
#print(f"O resultado do calculo é: {resultado} ")


# Escreva um programa que calcule a área de um circulo, recebendo o raio como entrada.

# Criando a variavel que irá receber o valor do raio
#raio_do_circulo = float(input("Digite o valor do raio "))

# Determinando a área do circulo.
#area_do_circulo = math.pi * raio_do_circulo ** 2
#print(f"Área do circulo é: {area_do_circulo:.2f}")

# Escreva um que peça ao usuário para digitar uma data no formato dd/mm/aaaa e , em seguida, imprima o dia, o mês; e o ano separadamente.

#Recebe a data informada pelo usuario.
data = input("Insira uma data no formato dd/mm/aaaa: ")

#Recebe a data informada pelo usuario, já separada com a função split
lista_dia_mes_ano = data.split("/")

#Imprimindo a data na tela, de acordo com a posição de cada elemento na lista.
print(f"O elemento 1 e o: {lista_dia_mes_ano[0]}")
print(f"O elemento 2 e o: {lista_dia_mes_ano[1]}")
print(f"O elemento 3 e o: {lista_dia_mes_ano[2]}")


