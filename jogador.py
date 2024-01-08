class Jogador:
    def __init__(self, nome, saldo, pontos):
        self.nome = nome
        self.saldo = saldo
        self.pontos = pontos
        self.mao = []


    def get_nome(self):
        return self.nome

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def set_mao(self, mao_jogador):
        self.mao = mao_jogador

    def get_mao(self):
        return self.mao


