import random

def inicio_jogo():
    print("--- Jogo: Corrida para o 100 ---")
    print("--- Opções de jogo ---")
    print(" -> Modo 1: O Computador joga primeiro ")
    print(" -> Modo 2: Tu jogas primeiro, o computador em segundo lugar")

    opcao_valida = 0

    while opcao_valida != 1 and opcao_valida != 2:
        try:
            opcao_valida = int(input("Escolhe o modo em que queres jogar, 1 ou 2: "))

            if opcao_valida != 1 and opcao_valida != 2:
                print("Essa opção de modo de jogo não é válida! Tenta novamente: ")

        except ValueError:
            print("Valor inválido! Tens de escrever um número inteiro: ")

    if opcao_valida == 1:
        jogo_computador_primeiro()
    elif opcao_valida == 2:
        jogo_computador_segundo()

def jogo_computador_primeiro():
    total = 0
    print("\n--- Modo 1: O Computador Joga Primeiro ---")
    print("--> O total começa em zero(0) ")

    totais_seguros = list(range(1,101,11))

    jogada_inicial = totais_seguros[0]
    total = total + jogada_inicial
    print(f"O computador joga primeiro e escolhe: {jogada_inicial} -> Total atual: {total}")

    while total < 100:
        userjoga_valido = False
        while userjoga_valido == False:
            try:
                user_joga = int(input("É a tua vez! Escolhe um número de 1 a 10: "))

                if user_joga < 1 or user_joga > 10:
                    print("Valor inválido! Tem de ser um número inteiro de 1 a 10: ")
                else:
                    userjoga_valido = True

            except ValueError:
                print("Valor inválido! Tens de escrever um número inteiro: ")

        total = total + user_joga
        print(f"Total após a tua jogada: {total}")

        if total == 100:
            print("Parabéns! Venceste o jogo!")
            break

        proximo = [x for x in totais_seguros if x > total]  #Cria uma lista só com os resultados seguros que ainda n foram usados
        comp_joga = proximo[0] - total
        total = total + comp_joga
        print(f"O computador escolhe: {comp_joga}. Total atual: {total}")

        if total == 100:
            print("O computador venceu!")
            break

def jogo_computador_segundo():
    total2 = 0
    print("\n--- Modo 2: O Computador Joga em Segundo Lugar ---")
    print("--> O total começa em zero(0) ")

    totais_seguros2 = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]

    while total2 < 100:
        userjoga2_valido = False
        while userjoga2_valido == False:
            try:
                user_joga2 = int(input("Começas tu! Escolhe um número de 1 a 10: "))

                if user_joga2 < 1 or user_joga2 > 10:
                    print("Valor inválido! Tem de ser um número inteiro de 1 a 10: ")
                else:
                    userjoga2_valido = True

            except ValueError:
                print("Valor inválido! Tens de escrever um número inteiro: ")

        total2 = total2 + user_joga2
        print(f"Total após a tua jogada: {total2}")

        if total2 == 100:
            print("Parabéns! Venceste o jogo!")
            break

        if total2 in totais_seguros2:
            if 100 - total2 < 10:
                max = 100 - total2
            else:
                max = 10

            comp_joga2 = random.randint(1, max)
        else:
            proximo2 = [y for y in totais_seguros2 if y > total2]
            comp_joga2 = proximo2[0] - total2

        total2 = total2 + comp_joga2
        print(f"O computador escolhe: {comp_joga2}. Total atual: {total2}")

        if total2 == 100:
            print("O computador venceu!")
            break

inicio_jogo()
