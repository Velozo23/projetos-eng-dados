import math

# Escreva um programa que soma 2 numeros inteiros inseridos pelo usuário.

# Recebe um numero digitado pelo usuário.
n1 = int(input("Digite um numero: "))

# Recebe outro numero digitado pelo usuário.
n2 = int(input("Digite outro numero: "))
#Realiza o calculo da operação
resultado = n1 // n2 
print(f"O resultado do calculo é: {resultado} ")


# Escreva um programa que calcule a área de um circulo, recebendo o raio como entrada.

# Criando a variavel que irá receber o valor do raio
raio_do_circulo = float(input("Digite o valor do raio "))

# Determinando a área do circulo.
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"Área do circulo é: {area_do_circulo:.2f}")
