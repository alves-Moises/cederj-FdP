from frente import frente_play
from servico import servico_play
from telhado import telhado_play

# pede pro usuario escolher a entrada e valida a escolha
def check_museum():
    valid = False
    while not valid:
        print("Escolha por onde entrar no museu: ")
        print("-frente\n-servico\n-telhado\n")
        choice = input("Sua escolha: ").lower()

        if( choice in ["frente", "servico", "telhado"] ):
            valid = True
        else:
            print("Responsta inválida...")

    return choice

def play_game():
    # first step:
    
    # escolha será executada de forma dinâmica
    museum = {
        "frente": frente_play,
        "servico": servico_play,
        "telhado": telhado_play
    }

    choice = check_museum()

    # executa a entrada pelo local escolhido
    museum[choice]()

    #seccond step

    #third step