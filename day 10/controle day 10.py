def adição(n1,n2):
    return n1+n2
def subitração(n1,n2):
    return n1-n2
def mutiplicaçao(n1,n2):
    return n1*n2
def diviçao(n1,n2):
    return n1/n2

calculadora={ "+" : adição , "-" : subitração , "*" : mutiplicaçao , "/" : diviçao   }
numero1=int(input("qual e o primeiro numero"))
controle =True
respostar=numero1
while  controle ==True:
    numero1=respostar
    operaçao= input("voce quer fazer qual operação matematica")
    numero2=int(input("qual e o segundo numero"))
    calculadora2=calculadora[operaçao]
    respostar=calculadora2(numero1,numero2)
    print(f"{numero1} {operaçao} {numero2} = {respostar}")
    controle2= input("digite nao para para").lower
    if controle2 =="nao":
        controle==False 