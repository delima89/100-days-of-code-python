
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ci=0
te=[]
te2=[]
te3=""
def encrypt(text,shift):
    text=list(text)
    count=0
    ci=0
    te=[]
    te2=[]
    te3=""
    for letter in text:
        ci=alphabet.index(text[count])
        te=alphabet[ci+shift]
        te2+=te
        te3+=str(te2[count])
        count+=1
    print(f"here you encode messange :{te3} !")

def decode(text,shift):
    text=list(text)
    count=0
    ci=0
    te=[]
    te2=[]
    te3=""
    for letter in range(1,len(text)+1):
        ci=alphabet.index(text[count-shift])
        te=alphabet[ci-shift]
        te2+=te
        te3+=str(te2[count])
        count+=1
    print(f"here you decode messange :{te3} !")
yes=""
while not yes =="no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if str(direction) == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decode(text,shift)
    yes=input("digite yes para fazer denovo ou no para encerra")



