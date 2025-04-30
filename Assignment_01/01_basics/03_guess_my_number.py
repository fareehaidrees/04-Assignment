import random

def main():
    secret_number = random.randint(1, 99)    

    print("I am thinking of a number between 0 and 99...")

    while True:
         guess_number = int(input("Enter a guess: "))

         if guess_number > secret_number:
             print("Your guess is too high")
         elif guess_number < secret_number:
             print(" Your guess is too low")
         else :
             print("Congrats! The number was: ", secret_number )
             break
         break

if __name__ == '__main__':
    main()