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

def 

# funcao principal
def main():
    Continue = True


    while Continue:
        
        choice = check_museum()


# inicializacao do programa
if __name__ == "__main__":
    main()
        