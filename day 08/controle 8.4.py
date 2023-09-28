
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    codigo=""
    for letter in text:
        posição=alphabet.index(letter)
        nova_posição=posição+shift
        nova_letra=alphabet[nova_posição]
        codigo+=nova_letra
    print(f"aqui esta sua mesangem codificada :{codigo} !")

def decode(text,shift):
    codigo=""
    for letter in text:
        posição=alphabet.index(letter)
        nova_posição=posição-shift
        nova_letra=alphabet[nova_posição]
        codigo+=nova_letra
    print(f"aqui esta sua mensagem decodificado :{codigo} !")
yes=""
while not yes =="no":
    direction = input("digite 'encode' para codificado, degite 'decode' to decodificado:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("digite um numero entre 1 e 9:\n"))
    if str(direction) == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decode(text,shift)
    yes=input("digite yes para fazer denovo ou no para encerra\n")



