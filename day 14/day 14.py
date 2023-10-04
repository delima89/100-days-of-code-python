import game_data 


import random

compa=random.randint(1,49)

comparaçao_A=game_data.data[compa]

right_aswer=True

pont=0

while right_aswer:
    print("""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
""")

    print(f"{comparaçao_A['name']}, a {comparaçao_A['description']}, from {comparaçao_A['country']} ")
   
    compa1=random.randint(1,49)

    comparaçao_B=game_data.data[compa1]

    print("""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
""")

    print(f"{comparaçao_B['name']}, a {comparaçao_B['description']}, from {comparaçao_B['country']} ")

    i=input("Quem tem mais seguidores? A ou B\n").lower()

    if i == "a":

        if comparaçao_A['follower_count']>comparaçao_B['follower_count']:
            
            pont+=1

            print(f"voce acerotou, sua pontuação é : {pont}")
            
            comparaçao_A=comparaçao_B
        else:
            print(f"desculpe, voce errou, sou pontuação final: {pont}")

            right_aswer=False
    elif i == "b":

        if comparaçao_A['follower_count']<comparaçao_B['follower_count']:
            
            pont+=1

            print(f"voce acerotou, sua pontuação é : {pont}")

            comparaçao_A=comparaçao_B
        else:
            print(f"desculpe, voce errou, sou pontuação final: {pont}")

            right_aswer=False
      

