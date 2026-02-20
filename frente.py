#entrda pela frente
def frente_play():
    print("Entrada de frente:")
    def check_input():
        valid = False()
        while not valid:
            values = input("Digite três valores:")

            try:
                values = input("Digite três valores:")
                values = values.split()

                x = int(values[0])
                y = int(values[1])
                z = float(values[2])
                
                arr_values = [x, y, z]
            except ValueError:
                print("Valores incorretos...")
            except IndexError:
                print("Esperava-se TRÊS valores...")
            else:
                valid = True

        return arr_values

    def check_combination(x, y, z):
        return ((294 / x == y) and (y / x == z))


    def play():
        Passed = False
        Lifes = 3
        while (not Passed) and (Lifes > 0):
            values = check_input()
            Passed += check_combination(*values)

            if not Passed:
                Lifes -= 1
                print("Combinação incorreta.")
                print(f"Vidas restantes: {Lifes}")

        print("=" * 30)
        print("\nPróxima etapa...\n")

        return {
            "Passed": Passed,
            "Lifes": Lifes
        }

    print("Entrada de frente:")

    return play()
