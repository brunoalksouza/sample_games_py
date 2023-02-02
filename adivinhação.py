import random

def jogar():
  print ("------------------------------")
  print ("   jogo de adivinhar numero   ")
  print ("------------------------------")
  
  valor_max = 100
  numero_secreto = random.randrange(0, valor_max)
  rodadas = 1
  tentativas = 0
  
  dificuldade = int(input("\nEscolha a dificuldade do seu jogo:\n 1-Fácil 2-Médio 3-Hard\n"))
  
  if (dificuldade == 3):
    tentativas = 5
    print("------------------------------------")
    print("\nVocê tem {} tentativas\n".format(tentativas))
      
  if (dificuldade == 2):
    tentativas = 7
    print("------------------------------------")
    print("\nVocê tem {} tentativas\n".format(tentativas))
      
  if (dificuldade == 1):
    tentativas = 10
    print("------------------------------------")
    print("\nVocê tem {} tentativas\n".format(tentativas))
    
  if (dificuldade < 1 or dificuldade > 3):
    print("\nSeu burro, pedi de 1 a 3")
  
    
  for rodada in range (1, tentativas+1):
  
    chute_str = input("Digite um número entre 0 e {}: ".format(valor_max))
    print("Você chutou: ", chute_str)
    chute = int(chute_str)
  
    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto
    
    if (acertou): 
      print("------------------------------------")
      print("\nParabens voce acertou o numero! \n")
      print("Sua pontuação é {} de {}".format(tentativas - rodadas, tentativas))
      print("------------------------------------")
      break
  
    if (rodadas == tentativas):
      print("------------------------------------\n")
      print("O número era: {}".format(numero_secreto))
      print("Exedeu o número de rodadas SEU BURRO!")
    
    elif (menor):
      print("------------------------------------")
      print("\nTentativa {} de {}".format(rodadas+1, tentativas))
      print("Você errou! Tente um numero maior \n")
      rodadas = rodadas+1
      
    elif (maior):
      print("------------------------------------")
      print("\nTentativa {} de {}".format(rodadas+1, tentativas))
      print("Você errou! Tente um numero menor \n")
      rodadas = rodadas+1

  print("---------------------------------")
  print("------ Fim de jogo ------")

if(__name__=="__main__"):
  jogar()