dias_semana = str(input("What's the day of the week? "))

match dias_semana:
    case "1":
        print("segunda")
    case "2":
        print("terça")
    case "3":
        print("quarta")
    case "4":
        print("quinta")
    case "5":
        print("sexta")
    case _:
        print("Você digitou errado.")