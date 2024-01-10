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
            print(f"\nOlá {jogador.nome}, você tem {jogador.saldo} klebinhos.")

            # Permitindo que o jogador decida quantas fichas comprar e adicione ao seu personagem
            fichas_comprar = int(input("Quantas fichas você deseja comprar? "))
            valor_fichas = 10 * fichas_comprar

            if valor_fichas <= jogador.saldo:
                jogador.saldo -= valor_fichas
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
                print(f"Agora você tem {fichas_comprar * 10} fichas e {jogador.saldo} klebinhos restantes.")
                print(""
                      ""
                      "")
            else:
                print("Saldo insuficiente para comprar essa quantidade de fichas.")
    except ValueError:
        print("Insira um número inteiro")



import random

def sorteio_e_vencedores(jogadores):
    def calcular_pontuacao(mao):
        return sum(mao)

    def determinar_vencedor(pontuacoes):
        pontuacoes_validas = [pontuacao for pontuacao in pontuacoes if pontuacao <= 21]

        if not pontuacoes_validas:
            return None

        return max(pontuacoes_validas)

    for jogador in jogadores:
        mao_jogador = jogador.mao
        print(f"{jogador.nome}, sua mão inicial é: {mao_jogador}")
        parou = False

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

    pontuacoes = [calcular_pontuacao(jogador.mao) for jogador in jogadores]
    vencedor = determinar_vencedor(pontuacoes)

    if vencedor is None:
        print("Todos os jogadores ultrapassaram 21! Não há vencedor nesta rodada.")
    else:
        vencedor_nome = [jogador.nome for jogador in jogadores if calcular_pontuacao(jogador.mao) == vencedor][0]
        print(f"{vencedor_nome} venceu com {vencedor} pontos!")

# Restante do código permanece igual


'''ele pergunta uma vez a cada jogador pois o jogo pressupoe que os mesmos não saibam 
    a mao um do outro assim como é no 21 real'''













if __name__ == "__main__":
    jogadores = criar_jogadores()
    realizar_apostas(jogadores)
    sorteio_e_vencedores(jogadores)
