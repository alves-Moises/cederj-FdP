def servico_play():
    def check_input():
        valid = False
        while not valid:

            try:
                values = input("Digite dois valores:")
                values = values.split()

                x = int(values[0])
                y = int(values[1])
                
                arr_values = [x, y]
            except ValueError:
                print("Valores incorretos...")
            except IndexError:
                print("Esperava-se DOIS valores...")
            else:
                valid = True

        return arr_values

    def check_combination(x, y):
        return ((x % y == 0) and (y % 2 == 1) and ( (x + y) > 50))
    

    Lifes = 3
    Passed = False
    while (not Passed) and (Lifes > 0):
        values = check_input()
        Passed += check_combination(*values)

        if not Passed:
            Lifes -= 1
            print("Combinacao incorreta.")
            print(f"Vidas restantes: {Lifes}")

    print("=" * 30)
    print("\nPróxima etapa...\n")

    print("Entrada por servico:")

    return {
        "Passed": Passed,
        "Lifes": Lifes
    }