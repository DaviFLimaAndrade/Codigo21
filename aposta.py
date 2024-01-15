from main import menu

def realizar_apostas(jogadores):
    try:
        for jogador in jogadores:
            if jogador.ficha <= 0:
                print("Suas fichas acabaram, agora seu terreno é nosso kkkk")
                print("Voltou ao menu inicial")
                print("-"*60)

            else:
                print('-' * 60)
                print(f"\nOlá {jogador.nome}, quantos klebinhos deseja apostar nesta rodada?")

                # Permitindo que o jogador decida quantos klebinhos apostar e subtraia das suas fichas
                while True:
                    try:
                        klebinhos_apostar = int(
                            input("Quantos klebinhos você deseja apostar? (Digite 0 para não apostar) "))
                    except ValueError:
                        print("Por favor, insira um número inteiro.")
                        continue

                    # Verificando se o jogador deseja apostar ou não
                    if klebinhos_apostar == 0:
                        print(f"{jogador.nome} escolheu não apostar nesta rodada.")
                        break

                    # Verificando se o jogador tem klebinhos suficientes para a aposta
                    if klebinhos_apostar > jogador.ficha:
                        print("Você não tem klebinhos suficientes para esta aposta. Tente novamente.")
                        continue

                    # Atualizando a aposta e subtraindo klebinhos do saldo do jogador
                    jogador.aposta = klebinhos_apostar
                    jogador.ficha -= klebinhos_apostar

                    print('-' * 60)
                    print(f"{jogador.nome}, você apostou {klebinhos_apostar} klebinhos nesta rodada.")
                    print("\n")
                    break

    except ValueError:
        print("Insira um número inteiro.")
