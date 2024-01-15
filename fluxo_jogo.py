from criando_avatar import criar_jogadores
from logica_jogo import sorteio_e_vencedores
from aposta import realizar_apostas

def fluxo():
    jogadores = criar_jogadores()
    sorteio_e_vencedores(jogadores)

    print("acabou")
