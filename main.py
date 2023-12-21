import random
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


def jogo(jogadores):
    cartas = [10]
    mao_jogador = []

    print('''             __   __      ________       ___ __ __      ______       ______              __           ________      
            /_/\ /_/\    /_______/\     /__//_//_/\    /_____/\     /_____/\             /_/\         /_______/\     
            \:\ \\ \ \   \::: _  \ \    \::\| \| \ \   \:::_ \ \    \::::_\/_            \:\ \        \::: _  \ \    
             \:\ \\ \ \   \::(_)  \ \    \:.      \ \   \:\ \ \ \    \:\/___/\            \:\ \        \::(_)  \ \   
              \:\_/.:\ \   \:: __  \ \    \:.\-/\  \ \   \:\ \ \ \    \_::._\:\            \:\ \____    \:: __  \ \  
               \ ..::/ /    \:.\ \  \ \    \. \  \  \ \   \:\_\ \ \     /____\:\            \:\/___/\    \:.\ \  \ \ 
                \___/_(      \__\/\__\/     \__\/ \__\/    \_____\/     \_____\/             \_____\/     \__\/\__\/ 
             
                                                                                                 ''')
    jogada = True
    contador = 0
    while jogada == True:
        try:
            for jogador in jogadores:
                opcao = int(input(f"{jogador.get_nome()}, Deseja comprar mais cartas? "
                                  "\n1: Sim"
                                  "\n2: Não"
                                  "\nDigite: "))

                carta = random.choice(cartas)
                mao_jogador = jogador.get_mao()  # um dos erros que enfrentei foi porque o append so funciona se o valor
                mao_jogador.append(carta)  # da lista estiver zerado
                jogador.set_mao(mao_jogador)
                mao_atual = sum(jogador.get_mao())
                int(mao_atual) # aqui eu converto como int para fazer a comparação lógica no if

                if opcao == 1 and mao_atual < 21:
                    var = contador + 1
                    print('-'*80)
                    print(f"{jogador.get_nome()} sua mão é: {mao_atual}")
                    print('-'*80)
                elif mao_atual > 21:
                    print(f"{jogador.get_nome()} Você ganhou {mao_atual}")
                    jogada = False
                    break
                else:
                    print("olalalallalalalalalalala")
        except ValueError:
            print("Insira um numero inteiro por favor")


if __name__ == "__main__":
    jogadores = criar_jogadores()
    realizar_apostas(jogadores)
    jogo(jogadores)
