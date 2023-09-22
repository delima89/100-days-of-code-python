import random

names_string = input("Diga o nome de todo as pessoas que vão paga a conta, separandos por virgulas. ")
names = names_string.split(",")
number=len(names)
numero=random.randint(0,(number-1))
print(f"{names[numero]},vai paga a conta hoje!")