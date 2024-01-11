from jogador import Jogador
class Jogo(Jogador, ):
    def __init__(self, nome, saldo):
        super().__init__(nome, saldo)

    def ranking(self):
        self.ranking ={self.nome:self.saldo}



