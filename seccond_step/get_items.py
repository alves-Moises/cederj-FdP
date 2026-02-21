def select_item():
    items = {"lanterna", "chave", "corda"}
    valid = False

    while not valid:
        valid = True
        print("lanterna - chave - corda")
        try:
            # tratamento já prevenindo duplicidade
            item_list = set(input("Selecione dois itens:").lower().split())

        except:
            print("Digite novamente")
        else:
            if(len(item_list) != 2):
                valid = False

            for item in item_list:
                if(not(item in items)):
                    print("Entrada inválida")
                    valid = False
                    break

    return item_list
            