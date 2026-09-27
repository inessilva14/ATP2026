# Modalidade 1: Computador pensa num número (0 a 100) e o utilizador tenta adivinhar

import random

def mod1():
    num1 = random.randint(0,100)
    tentativas1 = 0
    palpite1 = int(input("Pensei num número entre 0 e 100. Tenta adivinhar qual é: "))

    while palpite1 < 0 or palpite1 > 100:
        print("!! Valor inválido. Tem de ser um número inteiro entre 0 e 100. !!")
        palpite1 = int(input("Introduz um número entre 0 e 100: "))

    while palpite1 != num1:

        tentativas1 = tentativas1 + 1

        if palpite1 < num1:
            print("O número que pensei é Maior.")
        else:
            print("O número que pensei é Menor.")

        palpite1 = int(input("Ainda não acertaste. Tenta outra vez: "))

    tentativas1 = tentativas1 + 1
    print(f"Parabéns! Acertaste! O número é {num1} e usaste {tentativas1} tentativas.")

# Modalidade 2: O utilizador pensa num número (0 a 100) e o computador tenta adivinhar

def mod2():
    min = 0
    max = 100
    tentativas2 = 0

    print("Pensa num número de 0 a 100 e eu vou tentar adivinhar! ")
    num2 = random.randint(min,max)
    tentativas2 = tentativas2 + 1
    print(f"Será que o número que pensaste é {num2}? ")
    resposta = resposta_correta2()

    while resposta != "c":

        tentativas2 = tentativas2 + 1

        if resposta == "maior":
            min = num2 + 1
        else:
            max = num2 - 1

        num2 = random.randint(min,max)
        print(f"Será que o número que pensaste é {num2}? ")
        resposta = resposta_correta2()

    print(f"Boa, consegui acertar! Precisei de {tentativas2} tentativas.")

def resposta_correta2():
    respostac = input("Responde 'c' para Certo, 'maior' para caso o teu número seja Maior e 'menor' para caso o teu número seja Menor: ")

    while respostac != "c" and respostac != "maior" and respostac != "menor":
        print("!! Resposta inválida. Escreve apenas 'c', 'maior' ou 'menor' !! ")
        respostac = input("Responde 'c' para Certo, 'maior' para caso o teu número seja Maior e 'menor' para caso o teu número seja Menor: ")

    return respostac

# Modo principal: Para escolher qual modalidade queremos

def mod_principal():
    print("=== Jogo: Adivinha o número ===")
    print("=== Opções de jogo ===")
    print("  - Modalidade 1: O computador pensa, tu adivinhas")
    print("  - Modalidade 2: Tu pensas, o computador adivinha")

    opcao_valida = int(input("Escolhe a modalidade que queres jogar, 1 ou 2? "))

    while opcao_valida != 1 and opcao_valida != 2:
        print("Essa opção de modalidade não é válida. Tenta novamente! ")
        opcao_valida = int(input("Qual modalidade queres jogar, 1 ou 2? "))

    if opcao_valida == 1:
        mod1()
    elif opcao_valida == 2:
        mod2()
    
mod_principal()