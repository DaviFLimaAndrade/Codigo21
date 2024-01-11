import random

class Jogador:
    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo = saldo
        self._mao = self.sorteio()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def saldo(self):
        return self._saldo

    @property
    def mao(self):
        return self._mao

    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    def sorteio(self):
        baralho = {'A': 1, 'Q': 10, 'J': 10, 'K': 10,
                   '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9}
        mao = []

        for i in range(2):
            carta = random.choice(list(baralho.values()))
            mao.append(carta)

        return mao

