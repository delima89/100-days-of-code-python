import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
all=random.randint(0,nr_letters)
senha=[]
receba=0
tu=nr_letters+nr_numbers+nr_symbols
ju=""
ad=""
for l in range(1,int(nr_letters)+1):
    all=random.randint(0,nr_letters)
    senha.append(letters[all])
for s in range(1,int(nr_symbols)+1):
    all=random.randint(0,nr_symbols)
    senha.append(symbols[all])
for n in range(1,int(nr_numbers)+1):
    all=random.randint(0,nr_numbers)
    senha.append(numbers[all])
for senh in range(1,tu+1):
    ad=senha[receba]
    receba+=1
    ju+=ad
print(ju)