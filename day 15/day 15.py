from coffe import MENU
from coffe import resources
coffe_machine=True
def moedas():
    quarters=float(input("how many quarters?:"))
    v1=0.25
    dimes=float(input("how many dimes?:"))
    v2=0.10 
    nickles=float(input("how many nickles?:"))
    v3=0.05
    pennies=float(input("how many pennies?:"))
    v4=0.01
    totaol=quarters*v1+dimes*v2+nickles*v3+pennies*v4
    return totaol 
def cafe(tipo):

    escolha=MENU[tipo]

    comparaçao=escolha["ingredients"]
    
    custor=escolha["cost"]


    if resources["water"]<comparaçao["water"]:

        print("“Sorry there is not enough water.")
        return resources

    else:
        agua=resources["water"]-comparaçao["water"]
        resources["water"]=agua


    if resources["milk"]<comparaçao["milk"]:

        print("“Sorry there is not enough milk.")
        return resources

    else:
        leite=resources["milk"]-comparaçao["milk"]
        resources["milk"]=leite



   
    if resources["coffee"]<comparaçao["coffee"]:

        print("“Sorry there is not enough coffee.")
        return resources

    else:
        cafe=resources["coffee"]-comparaçao["coffee"]
        resources["coffee"]=cafe
        
    global total
    total=moedas()
    if total>=custor:
            troco=total-custor
            print(f"“Here is {round(troco,2)} dollars in change.” ")
            print(f"Here is your {tipo} ☕️. Enjoy!")
    elif  total<custor:
        print("Sorry that's not enough money. Money refunded.")

    custo=resources["cost"]+custor

    resources["cost"]=custo
    


    return resources

def espresso(tipo):

    escolha=MENU[tipo]

    comparaçao=escolha["ingredients"]
    
    custor=escolha["cost"]
    
    if resources["water"]<comparaçao["water"]:

        print("“Sorry there is not enough water.")
        return resources

    else:    
        agua=resources["water"]-comparaçao["water"]

        resources["water"]=agua

   
    if resources["coffee"]<comparaçao["coffee"]:

        print("“Sorry there is not enough coffee.")
        return resources

    else:
        cafe=resources["coffee"]-comparaçao["coffee"]

        resources["coffee"]=cafe
    
    global total
    total=moedas()
    if total>=custor:
            troco=total-custor
            print(f"“Here is {round(troco,2)} dollars in change.” ")
            print(f"Here is your {tipo} ☕️. Enjoy!")
    elif  total<custor:
        print("Sorry that's not enough money. Money refunded.")



    custo=resources["cost"]+custor

    resources["cost"]=custo
    

    return resources
def report():
    print("Water:",resources["water"] ,"ml")
    print("Milk:",resources["milk"] ,"ml")
    print("Coffee:",resources["coffee"] ,"g")
    print("money: $",resources["cost"])



while coffe_machine:
    
    caf=input("“What would you like? (espresso/latte/cappuccino):").lower()

    troco=0
    if caf == "report":
        report()
    elif caf=="off":
        coffe_machine=False
        break
    elif caf=="espresso":
        espresso(caf)
        escolha=MENU[caf]
        comparaçao=escolha["ingredients"]
        custor=escolha["cost"]

    elif caf == "latte" or caf=="cappuccino":
        cafe(caf)
        escolha=MENU[caf]
        comparaçao=escolha["ingredients"]
        custor=escolha["cost"]
