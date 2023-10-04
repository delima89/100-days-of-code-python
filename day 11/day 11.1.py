#blackjack=[cartas1(0),cartas1(0)]

def cartas1(carta1):
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta1 = random.choice(cards)
    return(carta1)
blackjack=[]
computador=[]
star="y"
while  star == "y":
    star=input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    conta=0
    conta1=0
    for i in range (2):
        blackjack.append(cartas1(0))
        conta+=blackjack[i]
        
    for e in range (2):
        computador.append(cartas1(0))
        conta1+=computador[e]

    count3=2
    print(f" Your cards:{blackjack}  , current score: {conta}")
    print(f" Computer's first card: {computador[0]} ")
    star=input("Type 'y' to get another card, type 'n' to pass:").lower()
    sta= True
    while star =="y":
        sta= False
        star== ""
        blackjack.append(cartas1(0))
        conta+=blackjack[count3]
        computador.append(cartas1(0))
        conta1+=computador[count3]
        count3+=1
        if conta ==21 and conta1>21:
            print(f" Your final hand:{blackjack}  , final score: {conta}")
            print(f"Computer's final hand: {computador}, final score: {conta1}")
            print ("You win")
            star =""
            break
        elif conta >21:
            print(f" Your final hand:{blackjack}  , final score: {conta}")
            print(f"Computer's final hand: {computador}, final score: {conta1}")
            print ("You went over. You lose")
            star =""
            break

        elif conta1>21:
            print(f" Your final hand:{blackjack}  , final score: {conta}")
            print(f"Computer's final hand: {computador}, final score: {conta1}")
            print("you win")
            star =""
            break
        elif conta1 ==21 and conta >21:
            print(f" Your final hand:{blackjack}  , final score: {conta}")
            print(f"Computer's final hand: {computador}, final score: {conta1}")
            print ("computer win")
            star =""
            break
        star== "t"
        print(f" Your cards:{blackjack}  , current score: {conta}")
        print(f" Computer's first card: {computador[0]} ")
        star=input("Type 'y' to get another card, type 'n' to pass:").lower()
if star ==True and conta < conta1 and conta1 <16:
    computador.append(cartas1(0))
    conta1+=computador[count3]

if conta < conta1 and sta== True :
    print(f" Your final hand:{blackjack}  , final score: {conta}")
    print(f"Computer's final hand: {computador}, final score: {conta1}")
    print ("You lose")


elif conta > conta1 and sta== True :
    print(f" Your final hand:{blackjack}  , final score: {conta}")
    print(f"Computer's final hand: {computador}, final score: {conta1}")
    print ("You win")


elif conta == conta1 and sta== True :
    print(f" Your final hand:{blackjack}  , final score: {conta}")
    print(f"Computer's final hand: {computador}, final score: {conta1}")
    print ("draw")