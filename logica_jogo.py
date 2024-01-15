import os
import random
from time import sleep
from aposta import realizar_apostas


def sorteio_e_vencedores(jogadores):
    def calcular_pontuacao(mao):
        return sum(mao)

    def determinar_vencedor(pontuacoes):
        pontuacoes_validas = [pontuacao for pontuacao in pontuacoes if pontuacao <= 21]

        if not pontuacoes_validas:
            return "Empate"

        pontuacao_maxima = max(pontuacoes_validas)

        if pontuacoes_validas.count(pontuacao_maxima) > 1:
            empate_pontuacoes = [pontuacao for pontuacao in pontuacoes_validas if pontuacao == pontuacao_maxima]
            return empate_pontuacoes

        return pontuacao_maxima

    continuar_jogando = True

    while continuar_jogando:
        '''for i in range(4):
            sleep(1)
            print(".")'''

        os.system("clear" if os.name == "posix" else "cls")

        # Realize as apostas no início de cada rodada
        realizar_apostas(jogadores)

        for jogador in jogadores:
            mao_jogador = jogador.sorteio()
            print(f"{jogador.nome}, sua mão inicial é: {mao_jogador}")
            parou = False

            if jogador.ficha > 0:
                print("Você pode jogar.")
            else:
                print("Você não pode jogar sem fichas.")

            while not parou:
                try:
                    opcao = int(input(f"{jogador.nome}, Deseja comprar mais cartas? "
                                      "\n1: Sim"
                                      "\n2: Não"
                                      "\nDigite: "))
                except ValueError:
                    print("Por favor, insira um número inteiro.")
                    continue

                if opcao == 1 and calcular_pontuacao(mao_jogador) <= 21:
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
                    mao_jogador.append(baralho[carta])
                    jogador.mao = mao_jogador

                    total_mao = calcular_pontuacao(mao_jogador)
                    print(f"{jogador.nome}, sua mão atual é: {total_mao}")

                    if total_mao > 21:
                        print(f"{jogador.nome} estourou com {total_mao} pontos!")
                        break
                else:
                    parou = True

            '''for i in range(4):
                sleep(1)
                print(".")'''

            os.system("clear" if os.name == "posix" else "cls")

        pontuacoes = [calcular_pontuacao(jogador.mao) for jogador in jogadores]
        vencedor = determinar_vencedor(pontuacoes)

        if vencedor == "Empate":
            print("Empate! Nenhum jogador venceu.")
        elif isinstance(vencedor, list):
            empate_pontuacoes = ", ".join(map(str, vencedor))
            print(f"Empate entre as pontuações: {empate_pontuacoes}, ninguém ganhou nada")
        else:
            vencedor_objeto = [jogador for jogador in jogadores if calcular_pontuacao(jogador.mao) == vencedor][0]
            vencedor_objeto.ficha += sum(jogador.aposta for jogador in jogadores)
            print(f"{vencedor_objeto.nome} venceu com {vencedor} pontos!")
            print(f"{vencedor_objeto.nome} agora possui {vencedor_objeto.ficha} fichas!")

        # Verifica se os jogadores desejam continuar jogando
        resposta = input("Deseja continuar jogando? (S para Sim / N para Não): ").upper()
        continuar_jogando = resposta == 'S'

    print("Jogo encerrado.")