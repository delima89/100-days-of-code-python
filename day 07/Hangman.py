import random
pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 

word_list =('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
display=[]
random.shuffle(word_list)
check=word_list[1]
count=0
count1=0
count2=1
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
for b in range (0,len(check)):
    display+=["_"]
print(f"{logo}\nBem vindo ao jogo da foca")
medida=display.count("_")
while display.count("_") >0:    
    count1+=1
    guess=str(input("diga uma letra")).lower()
    count=0
    meu = display.count("_")
    if count2 == 6:
        
        break
    for a in range (0,len(check)):
        a=check[0+count]
        count+=1
        if a== guess:
            display[count-1]=guess  
    if  meu == display.count("_") or meu> count:
        print(pics[count2])
        print(f"essa palavra não tem esssa letra {guess}")
        count2+=1   
    print(display)
if count2 ==6:
    print(pics[count2])
    print("Voce perdeu")
else:
    print("Voce ganhou")

    