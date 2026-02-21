from first_step.frente import frente_play
from first_step.servico import servico_play
from first_step.telhado import telhado_play
from seccond_step.get_items import select_item
from third_step.dark_room import final_stage


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
    print("Etapa 1:")
    player_stats = museum[choice]()

    if(player_stats["Lifes"] == 0):
        print("Fim de jogo")
        return
    
    # ================
    # seccond step
    item_list = select_item()
    player_stats["Items"] = item_list


    # ================
    # third step
    player_stats["Choice"] = choice

    final_stage(**player_stats)
    
        

    