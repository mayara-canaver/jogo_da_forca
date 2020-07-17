import sys
import textos
import jogo
import random

def instrucao():
    print("O jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra proposta,"
          " tendo como dica o número de letras e o tema ligado à palavra.\n"
          "A cada letra errada, é desenhada uma parte do corpo do enforcado.")
    return menu()

def menu():
    print("\n\n----------------- Bem Vindo ao Jogo da Velha -----------------\n")
    print("1 - Jogar")
    print("2 - Intruções")
    print("3 - Sair\n")
    x = int(input("Escolha uma opção:"))
    if x == 1:
        jogo.fase()
    elif x == 2:
        instrucao()
    elif x == 3:
        sys.exit()
    else:
        print(random.choice(textos.mensagem_erro))
        return menu()

menu()