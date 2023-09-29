termina=""
pessoas={}
aiorvalor=""
maiorvalor=1
print("Bem vindo ao leilão silencioso.")
while not termina == "nao":
    if 1 in range(1,2):
        paticipante=input("Qual e seu nome?\n")
        aporte=int(input("Qual e o valor do seu lance? apenas valores acima de R$100 \n$"))
        termina=input("Tem outro participante? sim ou nao ?.\n")
        pessoas[paticipante]=aporte
        if pessoas[paticipante] > maiorvalor:
            maiorvalor=pessoas[paticipante]
            aiorvalor=paticipante
  
print(f"o vencedor do leilão foi {aiorvalor} com lance de R${maiorvalor}.")
    