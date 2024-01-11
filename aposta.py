import logica_jogo

def realizar_apostas(jogadores):
    fichas = []
    contador = 1
    try:
        for jogador in jogadores:
            print('-' * 60)
            print(f"\nOlá {jogador.nome}, você tem {jogador.saldo} klebinhos.")

            # Permitindo que o jogador decida quantas fichas comprar e adicione ao seu personagem
            fichas_comprar = int(input("Quantas fichas você deseja comprar? "))
            valor_fichas = 10 * fichas_comprar
            fichas.append(fichas_comprar)

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
                contador += 1
            elif contador < jogadores:
                logica_jogo.sorteio_e_vencedores(jogadores)
                break

            else:
                print("Saldo insuficiente para comprar essa quantidade de fichas.")
    except ValueError:
        print("Insira um número inteiro")



