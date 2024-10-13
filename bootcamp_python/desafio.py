bonus_fixo = 1000

# Informa o nome do usuario
nome_usuario = input("Digite seu nome: ")

# Informa o valor do salario do usuario
salario_usuario = float(input("Digite o seu salario: "))

# Informa qual o valor do bonus do usuario
bonus_usuario = float(input("Digite o seu bonus: "))

# Calcula o valor do bonus do usuario
valor_do_bonus = bonus_fixo + salario_usuario * bonus_usuario

# Imprime uma mensagem personalizada, incluindo o nome do usuario e o bonus dele.
print(f"O usuario {nome_usuario} possui bonus de {valor_do_bonus}")


