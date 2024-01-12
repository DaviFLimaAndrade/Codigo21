from jogador import Jogador


def criar_jogadores():
    quantidade_jogadores = int(input("Insira quantos jogadores vamos acomodar: "))
    jogadores = []
    for i in range(quantidade_jogadores):  # Esse for vai gerar e adicionar em uma lista os meus jogadores
        print(f"CRIANDO CONTA JOGADOR {i + 1}".center(50))
        print()
        nome = input("Insira o nome do titular da conta: ")
        saldo = float(input("Insira o valor para depositar na conta: "))

        jogador = Jogador(nome, saldo, fichas=0)
        jogadores.append(jogador)
        print('-' * 60)

    return jogadores






