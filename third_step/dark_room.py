def final_stage(Passed, Lifes, Items, Choice):

    combination_list = {
        "frente": {
            "combination": {"lanterna", "chave"},
            "result": {
                3: "Excelente supremo",
                2: "Excelente",
                1: "Neutro"
            }
        },
        "servico": {
            "combination": {"chave", "corda"},
            "result": {
                3: "Perfeito supremo",
                2: "Perfeito",
                1: "Neutro"
            }
        },

        "telhado": {
            "combination": {"lanterna", "corda"},
            "result": {
                3: "Ninja supremo",
                2: "Ninja",
                1: "Neutro"
            }

        } 
    }

    if Items == combination_list[Choice]["combination"]:
        result = combination_list[Choice]["result"][Lifes]
    else:
        result = "Ruim"
        
    print("Você chegou a uma sala escura e encontra um cofre")
    print(f"Resultado final: {result}")