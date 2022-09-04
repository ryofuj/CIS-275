import random

def main():
    """
    user inputs the lower boudery and upper boudery of the range
    and the program prints all the numbers in the range.
    generate a random number in the range and the program prints.
    user guesses the random number.
    track the number of guesses.
    """
    lower = int(input("Enter the lower boudery: "))
    upper = int(input("Enter the upper boudery: "))
    random_number = random.randint(lower, upper)
    
    guess = int(input("Guess the random number: "))
    count = 1

    while guess != random_number:
        if guess < random_number:
            print("Too low")
        else:
            print("Too high")
        guess = int(input("Guess the random number: "))
        count += 1
    print("Correct, "+str(count)+" tries.")




main()