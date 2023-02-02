import adivinhação
import forca
import teste

def jogo():
  print("-----------------------")
  print("   Escolha um jogo     ")
  print("-----------------------\n")
  
  jogo = int(input("0->Teste * 1->Jogo da Adivinhação * 2->Jogo da Forca\n- "))

  if(jogo == 0):
    teste.jogar()
  
  if(jogo == 1):
    print("Você escolheu o Jogo da Adivinhação")
    print("------------------------------------")
    print("---------------------------------")
    adivinhação.jogar()
  
  if(jogo == 2):
    print("Você escolheu o Jogo da Forca")
    print("------------------------------------")
    print("---------------------------------")
    forca.jogar()

if(__name__=="__main__"):
  jogo()