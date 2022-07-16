def boliche (pino):
    for posicoes in pino:
        print(posicoes, end=" ")
    print()
    

estrutura_pinos = ["\n""I","","I","","I","","I","\n","","I","","I","","I","",
"\n","","","I","","I","","","\n","","","","I","","","","\n"]

valor_pinos = {

    "1" : 27,
    "2" : 18, 
    "3" : 20,
    "4" : 9,
    "5" : 11,
    "6" : 13,
    "7" : 0,
    "8" : 2,
    "9" : 4,
    "10": 6,
    
}

while True:
    boliche (valor_pinos)

    escolha = input("\nEscolha o pino que deseja derrubar: ")

    for pino in escolha:
        posicao=valor_pinos[pino]
        estrutura_pinos [posicao] = '_'
        
    boliche (estrutura_pinos)