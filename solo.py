import random
import os
from robo import Robo

def sorteio_e_vencedores_robo(jogadores):
    global jogador
    robo = Robo()

    def calcular_pontuacao(mao):
        return sum(mao)

    while True:
        os.system("cls" if os.name == "nt" else "clear")


        for jogador in jogadores:
            mao_jogador = jogador.sorteio()
            if sum(jogador.mao) <= 21:
                print(f"{jogador.nome}, sua mão inicial é: {mao_jogador}\n")

        mao_robo = robo.sorteio()
        robo.mao = mao_robo
        print(f"{robo.nome} sua mão inicial é: {mao_robo}\n")

        while True:
            opcao = int(input(f"{jogador.nome}, Deseja comprar mais cartas? "
                              "\n1: Sim"
                              "\n2: Não"
                              "\nDigite: "))

            if opcao == 1 and calcular_pontuacao(jogador.mao) <= 21:
                baralho = {
                    'zap_A': 1, 'ouro_A': 1, 'copas_A': 1, 'espadilha_A': 1,
                    'zap_2': 2, 'ouro_2': 2, 'copas_2': 2, 'espadilha_2': 2,
                    'zap_3': 3, 'ouro_3': 3, 'copas_3': 3, 'espadilha_3': 3,
                    'zap_4': 4, 'ouro_4': 4, 'copas_4': 4, 'espadilha_4': 4,
                    'zap_5': 5, 'ouro_5': 5, 'copas_5': 5, 'espadilha_5': 5,
                    'zap_6': 6, 'ouro_6': 6, 'copas_6': 6, 'espadilha_6': 6,
                    'zap_7': 7, 'ouro_7': 7, 'copas_7': 7, 'espadilha_7': 7,
                    'zap_8': 8, 'ouro_8': 8, 'copas_8': 8, 'espadilha_8': 8,
                    'zap_9': 9, 'ouro_9': 9, 'copas_9': 9, 'espadilha_9': 9,
                    'zap_10': 10, 'ouro_10': 10, 'copas_10': 10, 'espadilha_10': 10,
                    'zap_J': 10, 'ouro_J': 10, 'copas_J': 10, 'espadilha_J': 10,
                    'zap_Q': 10, 'ouro_Q': 10, 'copas_Q': 10, 'espadilha_Q': 10,
                    'zap_K': 10, 'ouro_K': 10, 'copas_K': 10, 'espadilha_K': 10,
                }

                carta = random.choice(list(baralho.keys()))
                jogador.mao.append(baralho[carta])
                total_mao = calcular_pontuacao(jogador.mao)
                total_mao_robo = robo.decidir_parada()

                print(f"{jogador.nome}, sua mão atual é: {total_mao}\n")
                print(f"{robo.nome}, sua mão atual é: {sum(robo.mao)}\n")
                print('-' * 60)

                if total_mao > 21 or sum(mao_robo) > 21:
                    print(f"{jogador.nome} estourou com {total_mao} pontos!\n")
                    print(f"{robo.nome} ganhou")
                    break
            elif opcao == 2:
                break

        total_mao_jogador = calcular_pontuacao(jogador.mao)
        total_mao_robo = calcular_pontuacao(mao_robo)

        print(f"Pontuação final: {jogador.nome}: {total_mao_jogador}, {robo.nome}: {sum(robo.mao)}")

        if total_mao_jogador > 21:
            print(f"{robo.nome} ganhou")
        elif total_mao_robo > 21:
            print(f"{jogador.nome} ganhou")
        elif total_mao_jogador > sum(robo.mao):
            print(f"{jogador.nome} ganhou")
        elif total_mao_robo > sum(robo.mao):
            print(f"{robo.nome} ganhou")
        else:
            print("Empate")

        novo_jogo = input("Deseja iniciar uma nova rodada? (s/n): ")
        if novo_jogo.lower() != 's':
            print("Jogo encerrado.")
            break
