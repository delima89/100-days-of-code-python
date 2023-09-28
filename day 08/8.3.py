n=0
def prime_checker(number=n):
    if n%2 ==0 or n%3 == 0 or n%7 == 0 or n%11 ==0 or n%13 == 0 or n%17 ==0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

#n=0
#def prime_checker(number=n):
    #primo=True
    #for i in range(2,number):
      #if  number%i == 0:
          #primo=False
    #if primo == True:
        #print("It's a prime number.")
    #else:
        #print("It's not a prime number.")
          
#n = int(input("Check this number: "))
#prime_checker(number=n)
