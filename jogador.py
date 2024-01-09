import random

class Jogador:
    def __init__(self, nome, saldo, pontos):
        self.nome = nome
        self.saldo = saldo
        self.pontos = pontos
        self.mao = self.sorteio()


    def get_nome(self):
        return self.nome

    def sorteio(self):
        cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        mao = []

        for i in range(2):
            carta = random.choice(cartas)
            mao.append(carta)

        return mao

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def set_mao(self, mao_jogador):
        self.mao = mao_jogador

    def get_mao(self):
        return self.mao


