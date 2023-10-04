def adição(n1,n2):
    return n1+n2
def subitração(n1,n2):
    return n1-n2
def mutiplicaçao(n1,n2):
    return n1*n2
def diviçao(n1,n2):
    return n1/n2
def calcula():
    print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)
    calculadora={ "+" : adição , "-" : subitração , "*" : mutiplicaçao , "/" : diviçao   }
    numero1=float(input("qual e o primeiro numero\n"))
    controle =True
    respostar=numero1
    while  controle==True:
        numero1=respostar
        operaçao= input("qual é a operação matematica\n")
        numero2=float(input("proximo numero\n"))
        calculadora2=calculadora[operaçao]
        respostar=calculadora2(numero1,numero2)
        print(f"{numero1} {operaçao} {numero2} = {respostar}")
        controle2= input(f"digite 'p' para encerra ou sim para continua a calcular com {respostar} ou digite 'y' para começar um novo calculor.\n")
        if controle2 =="p":
            controle=False
            break
        elif controle2 =="y":
            calcula() 
calcula() 