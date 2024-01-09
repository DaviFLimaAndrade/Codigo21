
from jogador import Jogador


def criar_jogadores():
    quantidade_jogadores = int(input("Insira quantos jogadores vamos acomodar: "))
    jogadores = []
    for i in range(quantidade_jogadores):  # Esse for vai gerar e adicionar em uma lista os meus jogadores
        print(f"CRIANDO CONTA JOGADOR {i + 1}".center(50))
        print()
        nome = input("Insira o nome do titular da conta: ")
        saldo = float(input("Insira o valor para depositar na conta: "))

        jogador = Jogador(nome, saldo, pontos=0)
        jogadores.append(jogador)
        print('-' * 60)
    return jogadores


def realizar_apostas(jogadores):
    try:
        for jogador in jogadores:
            print('-' * 60)
            print(f"\nOlá {jogador.get_nome()}, você tem {jogador.get_saldo()} klebinhos.")

            # Permitindo que o jogador decida quantas fichas comprar e adicione ao seu personagem
            fichas_comprar = int(input("Quantas fichas você deseja comprar? "))
            valor_fichas = 10 * fichas_comprar

            if valor_fichas <= jogador.get_saldo():
                jogador.set_saldo(jogador.get_saldo() - valor_fichas)
                print('''
                                                ###                                          ###
                                                 ##                                           ##
                      ####     ####     #####    ##                ####     ####     #####    ##
                     ##  ##       ##   ##        #####            ##  ##       ##   ##        #####
                     ##        #####    #####    ##  ##           ##        #####    #####    ##  ##
                     ##  ##   ##  ##        ##   ##  ##           ##  ##   ##  ##        ##   ##  ##
                      ####     #####   ######   ###  ##            ####     #####   ######   ###  ##
                    ''')
                print('-' * 60)
                print(f"Você comprou {fichas_comprar} fichas.")
                print(f"Agora você tem {fichas_comprar * 10} fichas e {jogador.get_saldo()} klebinhos restantes.")
            else:
                print("Saldo insuficiente para comprar essa quantidade de fichas.")
    except ValueError:
        print("Insira um numero inteiro")


import random


def sorteio_e_vencedores(jogadores):
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    pontuacoes_validas = {}
    todos_pararam = False

    while not todos_pararam:
        todos_pararam = True  # Supõe que todos pararam, mas verificamos abaixo

        for jogador in jogadores:
            mao_jogador = jogador.get_mao()

            print(f"{jogador.get_nome()}, sua mão inicial é: {mao_jogador}")

            opcao = int(input(f"{jogador.get_nome()}, Deseja comprar mais cartas? "
                              "\n1: Sim"
                              "\n2: Não"
                              "\nDigite: "))

            if opcao == 1:
                carta = random.choice(cartas)
                mao_jogador.append(carta)
                jogador.set_mao(mao_jogador)

                total_mao = sum(mao_jogador)
                print(f"{jogador.get_nome()}, sua mão atual é: {mao_jogador}")

                if total_mao > 21:
                    break  # Encerra o loop se a pontuação ultrapassar 21
                pontuacoes_validas[jogador.get_nome()] = total_mao

                todos_pararam = False  # Se alguém comprou, definimos como False

    if not pontuacoes_validas:
        print("Todos os jogadores ultrapassaram 21! Não há vencedor nesta rodada.")
    else:
        pontuacao_maxima = max(pontuacoes_validas.values())
        vencedores = [nome for nome, pontuacao in pontuacoes_validas.items() if pontuacao == pontuacao_maxima]

        if len(vencedores) == 1:
            print(f"{vencedores[0]} venceu com {pontuacao_maxima} pontos!")
        else:
            print("Empate! Os vencedores são:")
            for vencedor in vencedores:
                print(f"- {vencedor} com {pontuacao_maxima} pontos")


# Restante do código para criar jogadores, realizar apostas, etc.


if __name__ == "__main__":
    jogadores = criar_jogadores()
    realizar_apostas(jogadores)
    sorteio_e_vencedores(jogadores)
