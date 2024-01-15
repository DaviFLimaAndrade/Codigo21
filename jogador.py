import random


class Jogador:
    def __init__(self, nome, fichas):
        self.nome = nome
        self._fichas = fichas
        self._mao = self.sorteio()
        self._aposta = 0

    @property
    def ficha(self):
        return self._fichas

    @ficha.setter
    def ficha(self, quantidade_fichas):
        self._fichas = quantidade_fichas

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def mao(self):
        return self._mao

    @mao.setter
    def mao(self, nova_mao):
        self._mao = nova_mao

    @property
    def aposta(self):
        return self._aposta

    @aposta.setter
    def aposta(self, nova_aposta):
        self._aposta = nova_aposta

    def sorteio(self):
        baralho = {
            'zap_A': 1, 'ouro_A': 1, 'copas_A': 1, 'espadilha_A': 1,
            'zap_2': 2, 'ouro_2': 2, 'copas_2': 2, 'espadilha_2': 2,
            'zap_3': 3, 'ouro_3': 3, 'copas_3': 3, 'espadilha_3': 3,
            'zap_4': 4, 'ouro_4': 4, 'copas_4': 4, 'espadilha_4': 4,
            'zap_5': 5, 'ouro_5': 5, 'copas_5': 5, 'espadilha_5': 5,
            'zap_6': 6, 'ouro_6': 6, 'copas_6': 6, 'espadilha_6': 6,
            'zap_7': 7, 'ouro_7': 7, 'copas_7': 7, 'espadilha_7': 7,
            'zap_8': 8, 'ouro_8': 8, 'copas_8': 8, 'espadilha_8': 8,
            'zap_9': 9, 'ouro_9': 9, 'copas_9': 9, 'espadilha_9': 9,
            'zap_10': 10, 'ouro_10': 10, 'copas_10': 10, 'espadilha_10': 10,
            'zap_J': 10, 'ouro_J': 10, 'copas_J': 10, 'espadilha_J': 10,
            'zap_Q': 10, 'ouro_Q': 10, 'copas_Q': 10, 'espadilha_Q': 10,
            'zap_K': 10, 'ouro_K': 10, 'copas_K': 10, 'espadilha_K': 10,
        }

        mao = []

        for i in range(2):
            carta = random.choice(list(baralho.values()))
            mao.append(carta)

        self._mao = mao  # Atualiza a mão do jogador
        return mao

    def transferir_fichas(self, jogador_destino, quantidade):
        self._fichas -= quantidade
        jogador_destino._fichas += quantidade
