import random

def jogar():
    print("------------------------------")
    print("        jogo da forca         ")
    print("------------------------------")

    erros = 0
    acertou = False
    enforcou = False
  
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    posicao = random.randrange(0, len(palavras))
    palavra_secreta = palavras[posicao].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)
    
    while (not acertou and not enforcou):
        chute = input("------------------------------\nDigite uma letra: ")
        chute = chute.strip().upper()
        
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra == chute):
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1

        print(letras_acertadas)
        acertou = "_" not in letras_acertadas
        if(7-erros != 0):  
          print("\nVocê só pode errar {} vezes".format(7 - erros))

        if (erros == 1):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):

            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print("  _______     ")    
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print("  _______     ")
            print(" |/      |    ")  
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 6):
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print("PERDEU SEU MERDA!")
            print("A palavra era {}".format(palavra_secreta))
            print("    _______________        ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\   ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/    ")
            print(" |   XXX       XXX   |     ")
            print(" |                   |     ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |       ")
            print("   | I I I I I I I |       ")
            print("   |  I I I I I I  |       ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ")

        if (acertou):
            print("Parabéns, você ganhou!")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
            print("------ {} ------".format(palavra_secreta))

    
    print("------ Fim de jogo ------")


if (__name__ == "__main__"):
    jogar()
