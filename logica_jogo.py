import os
import random
from time import sleep


def sorteio_e_vencedores(jogadores):
    def calcular_pontuacao(mao):
        return sum(mao)

    def determinar_vencedor(pontuacoes):
        pontuacoes_validas = [pontuacao for pontuacao in pontuacoes if pontuacao <= 21]

        if not pontuacoes_validas:
            return None

        return max(pontuacoes_validas)

    
    for i in range(4):
            sleep(1)
            print(".")   
            
    os.system("cls")

    for jogador in jogadores:
        mao_jogador = jogador.mao
        print(f"{jogador.nome}, sua mão inicial é: {mao_jogador}")
        parou = False

        if jogador.ficha[0] > 0:
            print("pode jogar")
        else:
            print("pode não jogado")

        while not parou:
            opcao = int(input(f"{jogador.nome}, Deseja comprar mais cartas? "
                              "\n1: Sim"
                              "\n2: Não"
                              "\nDigite: "))

            if opcao == 1 and calcular_pontuacao(mao_jogador) <= 21:
                baralho = {'A': 1, 'Q': 10, 'J': 10, 'K': 10,
                           '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                           '7': 7, '8': 8, '9': 9}
                carta = random.choice(list(baralho.keys()))
                mao_jogador.append(baralho[carta])
                jogador._mao = mao_jogador

                total_mao = calcular_pontuacao(mao_jogador)
                print(f"{jogador.nome}, sua mão atual é: {total_mao}")

                if total_mao > 21:
                    print(f"{jogador.nome} estourou com {total_mao} pontos!")
                    break
            else:
                parou = True

        for i in range(4):
            sleep(1)
            print(".")

        os.system("cls")

    pontuacoes = [calcular_pontuacao(jogador.mao) for jogador in jogadores]
    vencedor = determinar_vencedor(pontuacoes)

    if vencedor is None:
        print("Todos os jogadores ultrapassaram 21! Não há vencedor nesta rodada.")
    else:
        vencedor_nome = [jogador.nome for jogador in jogadores if calcular_pontuacao(jogador.mao) == vencedor][0]
        print(f"{vencedor_nome} venceu com {vencedor} pontos!")

        '''ele pergunta uma vez a cada jogador pois o jogo pressupoe que os mesmos não saibam 
            a mao um do outro assim como é no 21 real'''