from criando_avatar import criar_jogadores
from logica_jogo import sorteio_e_vencedores
from solo import sorteio_e_vencedores_robo

def fluxo():
    jogadores = criar_jogadores()
    if len(jogadores) > 1:
        sorteio_e_vencedores(jogadores)
    else:
        print("\n SINGLE PLAYER ATIVADO \n")
        sorteio_e_vencedores_robo(jogadores)

