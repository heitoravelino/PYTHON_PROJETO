import os

def finalizar():
    # Limpa a tela de acordo com o sistema operacional
    os.system("cls")
    print("Obrigado pela informação.")

def par_impares(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um número, por favor: "))
finalizar()
print(f"O número que você informou é: {numero}, e ele é {par_impares(numero)}.")

def classificar_idade(idade):
    if idade <= 12:
        return "criança"
    elif idade <= 18:
        return "adolescente"
    else:
        finalizar()
        return "adulto"

idade = int(input("Digite sua idade: "))
print(f"Conforme a idade informada ({idade} anos), você é considerado: {classificar_idade(idade)}.")

usario_correto = ("Alura","alura")
senha_correta = "Alura123"

usuario = input("Digite o nome do usuário: ").lower()
senha = input("Digite sua senha: ")

if usuario in usario_correto and senha == senha_correta:
    print("******Login bem sucessido******")
else:
    print("Dados inválidos. Tente novamente !!!")

    numero = -1
for i in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    print(i)
    if numero > 0:
        break

print("Você digitou:", numero)