def main():
    #problem1()
    #problem2()
    #problem3()
    problem4()


#def problem1():
    #myName = input("My name is")
    #name = "Enricka"
    #print( myName ,name)
#main()


#def problem2():
    #extraCredit = int(input("how much extra credit did you earn?"))
    #if (extraCredit<5):
        #print("THAT'S NOT ENOUGH EXTRA CREDIT")
   # elif   (extraCredit>20):
       # print("THAT'S TOO MUCH EXTRA CREDIT")
#main()


#def problem3():
    #password = int(input("Enter a password!"))
    #samePassword = int(input("Enter your password again!"))
    #if  (password==samePassword):
        #print("CORRECT")
    #else:
       # print("THAT'S NOT CORRECT")
#main()

def problem4():
    card1 = int(input("Enter a card number."))
    card2= int(input("Enter another card number."))
    total = int(str(card1 + card2))
    if  (total==21):
        print("BLACKJACK")
    elif    (total>21):
        print("BUST")
main()


