import random

def game(attempts=0,max_attempts=10):

    """
    so welcome to the guessing game where we are going to
    guess some random number between 1 to 100
    well winner might not get anything ,but the clear understanding
    of using the function
    """
    number=random.randint(1,100)
    print("\n 🎲 welcome to guessing random number\n")
    print("\n i picked my number between 1 and 100\n:")
    print(f"you have {max_attempts} attempts left .All the best")

    while attempts < max_attempts:
        try:
            guess=int(input(f"{attempts+1} enter you guess:"))
            attempts+=1
            if guess == number:
                print(f"you have guessed the right answer {number}")
                break
            elif guess <number:
                print("you guess is low")
            else :
                print("your guess is high")
        except ValueError:
            print("invalid input")
            if attempts==max_attempts and guess!=number:
                print("you guessed the wrong answer")

def main():
    while True:
        game()
        replay=input("do you want to play again? (y/n)").lower()
        if replay !='y':
            print("thanks for playing")
            break


if __name__=='__main__':
    main()



