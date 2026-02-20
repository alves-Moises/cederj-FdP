from game import play_game
# funcao generica para validar entrada de valor inteiro
def check_int():
    valid = False
    while not valid:
        try:
            x = int(input())
        except ValueError:
            print("Resposta inválida")
        else:
            valid = True
    return x

# funcao principal
def main():
    Continue = True

    while Continue:
        play_game()
        
        Continue = input("Deseja continuar? 1 - Sim, 2 - não") == "1"
        print("=" * 30)
        
    print("Fim de jogo.")

# inicializacao do programa
if __name__ == "__main__":
    main()
