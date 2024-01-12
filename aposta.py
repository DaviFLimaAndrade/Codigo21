def realizar_apostas(jogadores):
    try:
        for jogador in jogadores:
            print('-' * 60)
            print(f"\nOlá {jogador.nome}, você tem {jogador.saldo} klebinhos.")

            # Permitindo que o jogador decida quantas fichas comprar e adicione ao seu personagem
            fichas = []
            while True:
                fichas_comprar = int(input("Quantas fichas você deseja comprar? "))
                valor_fichas = 10 * fichas_comprar
                fichas.append(valor_fichas)

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
                    print(f"Agora você tem {sum(fichas) * 10} fichas e {jogador.saldo} klebinhos restantes.")
                    print("\n")

                    mais_fichas = input("Deseja comprar mais fichas? (S para Sim / N para Não): ").upper()
                    if mais_fichas != 'S':
                        jogador._fichas = fichas  # setando as valores na lista de fichas dos jogadores
                        print(jogador.ficha)
                        break
                else:
                    print("Saldo insuficiente para comprar essa quantidade de fichas.")
    except ValueError:
        print("Insira um número inteiro")
