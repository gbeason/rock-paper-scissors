import time
from random import randint

def main():

    username = intro()
    time.sleep(1)
    
    KnowHow(username)
    time.sleep(1)

    ComputerChose = Comp()

    PlayerChose = Player()
    time.sleep(1)

    Result = game(ComputerChose,PlayerChose)

    GameMessage(PlayerChose,ComputerChose,Result)
    time.sleep(.1)

    PlayAgainQ()
    

def intro():

    print("\tGreeting player, what is your name?")
    username = input()

    return username

def KnowHow(username):

    print("\n\n\t"+username + " do you know how to play 'Rock, Paper, Scissors'?")
    time.sleep(.5)
    print("\t(Y) Yes\t(N) No")
    Know = input().upper()

    if Know != 'Y':
        if Know == 'N':
            print("\tThe player and computer must each select one of three choices.")
            time.sleep(1)
            print("\n\tThe choices are Rock, Paper, and Scissors.")
            time.sleep(1)
            print("\n\tRock > Scissors > Paper > Rock")
            time.sleep(1)
            print("\n\tWhoever's selection beats the other's selection wins.\n\n")
            time.sleep(1)

        else:
            print("Invalid input. Please try again.")
            KnowHow(username)

def game(ComputerChose,PlayerChose):


    if ComputerChose == PlayerChose:

        Result = 'Draw'


    elif PlayerChose == 'Rock':

        if ComputerChose == 'Paper':

            Result = 0
            
        if ComputerChose == 'Scissors':

            Result = 1

            
    elif PlayerChose == 'Paper':

        if ComputerChose == 'Rock':

            Result = 1

        if ComputerChose == 'Scissors':

            Result = 0


    elif PlayerChose == 'Scissors':

        if ComputerChose == 'Rock':

            Result = 0

        if ComputerChose == 'Paper':

            Result = 1


    return Result
    

def Comp():

    CompSelection = randint(1,3)

    if CompSelection == 1:
        CompTool = 'Rock'
    elif CompSelection == 2:
        CompTool = 'Paper'
    else:
        CompTool = 'Scissors'

    return CompTool
    
    
def Player():

    print("\tPlease make your selection...")
    print("\n\t(R) Rock\t(P) Paper\t(S) Scissors\n")
    Pselect = input().upper()

    if Pselect == "R":
        PWeapon = 'Rock'

    elif Pselect == "P":
        PWeapon = 'Paper'

    elif Pselect == "S":
        PWeapon = 'Scissors'

    else:

        print("\n\tInvalid input.  Please try again.")
        Player()

    return PWeapon


def GameMessage(PlayerChose,ComputerChose,Result):

    print('\n\n\tYou chose '+PlayerChose+'.')
    time.sleep(1)
    print('\t.')
    time.sleep(1)
    print('\t.')
    time.sleep(1)
    print('\t.')
    time.sleep(1)
    print("\tThe Computer chose "+ComputerChose+".")
    
    if Result == 'Draw':

        if ComputerChose == 'Rock':

            print("\n\n\tThe two rocks shattered against each other!")

        if ComputerChose == 'Paper':

            print("\n\n\tBoth yours and your opponent's papers were lost in the mail \n\twhen a mail truck collided with a fuel tanker and caught on fire!")

        if ComputerChose == 'Scissors':

            print("\n\n\tIn an ironic twist of fate, the blades of yours and your \n\topponent's scissors only succeeded in sharpening each other!")

    elif Result == 1:

        if PlayerChose == 'Rock':

            print("\n\n\tYour rock has crushed the dull blades of your opponent's scissors!")

        if PlayerChose == 'Paper':

            print("\n\n\tThe Computer's rock was little help against your written \n\tallegations in court!")

        if PlayerChose == 'Scissors':

            print("\n\n\tYour Scissors cut right through the red tape your \n\topponent tried to throw at you!")

    elif Result == 0:

        if ComputerChose == 'Rock':

            print("\n\n\tYour scissors were easily broken by the brute force \n\tof your opponent's rock!")

        if ComputerChose == 'Paper':

            print("\n\n\tYour rock was little help against the mountain of \n\tpaperwork your opponent laid out before you!")

        if ComputerChose == 'Scissors':

            print("\n\n\tYour evidence against your opponent was \n\teasily shredded by their annoying scissors!")

    else:

        print("THE UNIVERSE EXPLODED!!!")


def PlayAgainQ():

    print("\n\n\tWould you like to play again?\t\t\t(Y) Yes\t(N) No")
    YN = input().upper()

    if YN == 'Y':

        print("\n\tAlrighty then!\n\n\n\n\n\n\n\n\n\n")
        time.sleep(1)
        main()

    elif YN == 'N':

        print("\n\tOkay! See you later!")
        time.sleep(1)

    else:

        print("\n\tInvalid input.  Please try again.\n\n")
        PlayAgainQ()



main()
