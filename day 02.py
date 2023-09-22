print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
n=name1.lower()
n2=name2.lower()
a=n.count("t")+n.count("r")+n.count("u")+n.count("e")+n2.count("t")+n2.count("r")+n2.count("u")+n2.count("e")
b=n.count("l")+n.count("o")+n.count("v")+n.count("e")+n2.count("l")+n2.count("o")+n2.count("v")+n2.count("e")

love=(str(a)+str(b))
love1=int(love)
if love1 <10 or love1 > 90:
    print(f"Your score is {love}, you go together like coke and mentos.")
elif love1 >= 40 and love1 <=50:
    print(f"Your score is {love}, you are alright together."
)
else:
  print(f"Your score is {love1}.")