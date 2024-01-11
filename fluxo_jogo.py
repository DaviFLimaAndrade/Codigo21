import criando_avatar
import aposta
import logica_jogo

def fluxo():
    jogadores = criando_avatar.criar_jogadores()
    aposta.realizar_apostas(jogadores)
    logica_jogo.sorteio_e_vencedores(jogadores)

    print("acabou")