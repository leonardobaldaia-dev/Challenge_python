
def obter_informacoes_piloto():
    nome = input("Nome do piloto: ")
    equipe = input("Equipe: ")
    return nome, equipe

def simular_volta(energia_restante):
    energia_gasta = 5
    energia_restante -= energia_gasta
    return energia_restante

def corrida():
    nome, equipe = obter_informacoes_piloto()
    energia_restante = 100
    num_voltas = 10

    print(nome + " (" + equipe + ") - Largada!")

    for volta in range(1, num_voltas + 1):
        energia_restante = simular_volta(energia_restante)
        print("Volta " + str(volta) + ": Energia restante: " + str(energia_restante) + "%")

        if energia_restante <= 0:
            print("Bateria esgotada! Fim da corrida.")
            break 
    else:
        print(nome + " (" + equipe + ") completou a corrida!")

corrida()