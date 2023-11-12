from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def pedir_ano_nascimento():
    while True:
        try:
            ano = int(input("Por favor, digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Por favor, digite um ano válido.")

nome = input("Digite seu nome completo: ")
ano_nascimento = pedir_ano_nascimento()
idade = calcular_idade(ano_nascimento)

print(f"Olá, {nome}!")
print(f"No ano de 2022, você completou ou completará {idade} anos.")
