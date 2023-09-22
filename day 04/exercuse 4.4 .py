import random
computador=random.randint(0,2)
eu=int(input("What do you chosse? Type 0 for rock, 1 for Paper or 2 for Scissors."))
Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if  eu== 0:
    print(f"\n \nyou chose rock\n \n{Rock}")
    if computador == 0:
        print(f"your opponent chose rock :\n{Rock}\ndraw.")
    elif computador == 1:
        print(f"your opponent chose paper :\n{Paper}\nYou lose.")
    else:
        print(f"your opponent chose scissors:\n{Scissors}\nyou win.")
elif  eu== 1:
    print(f"\n \nyou chose paper\n \n{Paper}")
    if computador == 0:
        print(f"your opponent chose rock :\n{Rock}\nyou win.")
    elif computador == 1:
        print(f"your opponent chose paper:\n{Paper}\ndraw.")
    else:
        print(f"your opponent chose scissors:\n{Scissors}\nyou lose.")
elif  eu== 2:
    print(f"\n \nyou chose scissors\n \n{Scissors}")
    if computador == 0:
        print(f"your opponent chose rock :\n{Rock}\nyou lose.")
    elif computador == 1:
        print(f"your opponent chose paper:\n{Paper}\nyou win.")
    else:
        print(f"your opponent chose scissors:\n{Scissors}\ndraw.")
        