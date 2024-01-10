from jogador import Jogador

class Jogador:
    def __init__(self, nome, saldo=0, pontos=0):
        self.nome = nome
        self.saldo = saldo
        self.pontos = pontos
        self.mao = []  # A mão inicial do jogador será uma lista vazia

    def comprar_fichas(self, quantidade):
        # Lógica para adicionar fichas ao jogador

    def atualizar_vitorias(self):
        # Lógica para atualizar o número de vitórias do jogador

class Jogo:
    def __init__(self):
        self.jogadores = []
        self.numero_fichas = 0
        self.recordista = None
        self.numero_vitorias = 0

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def definir_recordista(self, jogador):
        self.recordista = jogador.nome

    def atualizar_vitorias(self, jogador):
        jogador.atualizar_vitorias()
        self.numero_vitorias +=