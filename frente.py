#entrda pela frente
def frente_play():
    print("Entrada de frente:")
    def check_input():
        valid = False()
        while not valid:
            values = input("Digite três valores:")

            try:
                values = values.split()

                x = int(values[0])
                y = int(values[1])
                z = float(values[2])
                
                arr_values = [x, y, z]
            except ValueError:
                print("Valores incorretos...")
            else:
                valid = True

        return arr_values

    def play(x, y, z):
        print(x, y, z)

    values = check_input()
    play(*values)
    lifes = 3
