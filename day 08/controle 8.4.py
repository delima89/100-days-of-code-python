def encrypt(text,shift,diretion):
    yes=0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while not yes =="no":
        direction = input("digite 'encode' para codificado, degite 'decode' to decodificado:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("digite um numero entre 1 e 9:\n"))
        shift = shift% 26
        codigo=""
        if direction == "encode":
            for char in text:
                if char in alphabet:
                    posição=alphabet.index(char)
                    nova_posição=posição+shift
                    nova_letra=alphabet[nova_posição]
                    codigo+=nova_letra
                else:
                    codigo+=char
            print(f"aqui esta sua mesangem codificada :{codigo} !")
        elif direction == "decode":
            for char in text:
                if char in alphabet:
                    posição=alphabet.index(char)
                    nova_posição=posição-shift
                    nova_letra=alphabet[nova_posição]
                    codigo+=nova_letra
                
                else:
                    codigo+=char
            print(f"aqui esta sua mesangem codificada :{codigo} !")        
        else:
            print("erro")
            print(f"aqui esta sua mensagem decodificado :{codigo} !")
        yes=input("digite yes para fazer denovo ou no para encerra\n")
direction = text = shift = codigo=""
print("obrigado")
encrypt(text,shift,direction)





