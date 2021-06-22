print("Sakshi Bheda\nWelcome ,This is Number Guesses Game")
n=18
guesses=1
print("Number of guesses is limited to only 9 times: ")
while (guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("congrates....you won ...!!!!!!!!\n")
        print("no.of guesses he took to finish.")
        break
    print(9-guesses,"no. of guesses left")
    guesses = guesses + 1

if(guesses>9):
    print("Game Over")
