#Random Number Guessing Game
#Objective: Program a random number guessing game between 1-100 If too High say so, if too low say so, have the number of guesses and give the option to restart the game
def main():
      
    import random
     
    inclusive_range = (1, 100)

    

    print("Guess a random number that is between 1 and 100 \n") #Intro
    target = random.randint(*inclusive_range)
    yeslist=["yes", "y", "yeah"] #different ways for yes
    answer, i = None, 0
    while True:
        answer != target
        i += 1
        txt = input("Your guess:") #what your guess is
        try:
            answer = int(txt)
        except ValueError:
            print("Letters and Characters are invalid. Please Submit a number between 1 to 100") #if error typing letters or characters 
            continue
        if answer < inclusive_range[0] or answer > inclusive_range[1]:
            print("That number is out of range. Please Submit a number between 1 to 100") #error if typing out of range between 1 to 100
            continue
        if answer == target:
            print("Congrats it took you %i guesses" % i) # prompt if guess correct and gives guesses total
            break
        if answer < target: print(" Too low, try again.") #error if guess is low
        if answer > target: print(" Too high, try again.")#error if guess is to high
        
    restart = input("Do you want to play again? Yes or No:") #restarting after game is won 
    if restart in yeslist:
        main()
    else:
        exit()


main()
