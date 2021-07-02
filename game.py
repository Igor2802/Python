import random

def gera():
    return random.randint(1,100)

def game():
    resposta = gera()
    tentativa = 0
    print("\nPalpite gerado!")

    chute=0
    while chute is not resposta:
        tentativa +=1
        chute = int(input("Qual o seu chute: "))
        if chute > resposta:
            print("Errou Bixooooo!")
        elif chute < resposta:
            print("Errou Bixooooo!")
        else:
            print("Parábens você acertou bixoooo!", resposta, "Acertou em", tentativa,"tentativas!")

while True:
    game()