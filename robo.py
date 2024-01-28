import random


class Robo:

    def __init__(self):
        self.nome = "Douglas Robo"
        self.mao = self.sorteio()

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
            carta = random.choice(list(baralho))
            mao.append(baralho[carta])

        return mao

    def decidir_parada(self):
        soma_mao = sum(self.mao)
        porcentagem = (soma_mao / 21) * 100  # Calcula a porcentagem da soma em relação a 21

        # Se a porcentagem estiver acima de 70% ou a soma for maior ou igual a 17, pare
        if porcentagem >= 70:
            return self.mao
        else:
            # Adiciona uma carta aleatória à mão do robô
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
            carta = random.choice(list(baralho.keys()))  # Escolhe uma chave aleatória
            self.mao.append(baralho[carta])
            return self.mao
