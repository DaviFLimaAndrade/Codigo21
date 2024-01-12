import fluxo_jogo
import os


def menu():
    os.system("cls")
    print("Ola Guerreiros(as), tudo bem?")
    opcao = int(input("\n1: Jogar"
                      "\n2: Ver ranking"
                      "\nDigite: "))

    if opcao == 1:
        print("")
        fluxo_jogo.fluxo()
    elif opcao == 2:
        pass


if __name__ == "__main__":
    menu()
