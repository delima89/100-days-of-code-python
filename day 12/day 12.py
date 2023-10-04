import random
numero=random.randint(1,100)
def adivinhaçao_facil():
    for i in range (10):
        print(f"voce tem {10-i} tentativas\n")
        aposta=int(input("faça sua apostar?\n"))
        if aposta > numero:
            print("muito altor\n")
        elif aposta < numero:
            print("muito baixo\n")
        elif aposta == numero:
            return aposta
             
def adivinhaçao_dificil():
    for i in range (5):
        print(f"voce tem {5-i} tentativas\n")
        aposta=int(input("faça sua apostar?\n"))
        if aposta > numero:
            print("muito altor\n")
        elif aposta < numero:
            print("muito baixo\n")
        elif aposta == numero:
            return aposta
            

print("Bem vindo ao jogo de adivinhaço de numeorõs\nEu estou pensado em um numero entre 1 e 100")
dificudade=str(input("escolha sua dificudade, 'facil' ou 'dificil'")).lower()
if dificudade== "facil":
    if adivinhaçao_facil() == numero:
        print(f"Voce acertou! O numero é {numero}")
    else:    
        print("Voce perdeu todas suas tentativas, Voce perdeu")
elif dificudade=="dificil":
    if adivinhaçao_dificil() == numero:
        print(f"Voce acertou! O numero é {numero}")
    else:    
        print("Voce perdeu todas suas tentativas, Voce perdeu")

