def telhado_play():

    def check_input():
        valid = False
        while not valid:
            try:
                values = input("Digite três valores:").split()
                x, y, z = values
                arr_values = [
                    float(x),
                    float(y),
                    float(z)
                ]

            except ValueError:
                print("Valores incorretos...")
            except IndexError:
                print("Esperava-se TRÊS valores...")
            else: valid = True
        
        return arr_values

    def check_combination(x, y, z):
        return ((x + y > z) and (x + z > y) and (y + z > x))

    def play():
        Passed = False
        Lifes = 3

        while (not Passed) and (Lifes > 0):
            values = check_input()
            Passed += check_combination(*values)

            if not Passed:
                Lifes -= 1
                print("Combinacao incorreta")
                print(f"Vidas restantes: {Lifes:^10}")

        return {
            "Passed": Passed,
            "Lifes": Lifes
        }

    
    print("Entrada por telhado...")
    play()