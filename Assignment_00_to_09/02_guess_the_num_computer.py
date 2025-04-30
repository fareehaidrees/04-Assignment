import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != "c":
        random_number = random.randint(low, high)

        feedback = input(f"Is {random_number} too High (H), too Low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = random_number -1

        elif feedback == "l":
           low = random_number +1

    print(f'The computer guessed your number {random_number} correctly!!')
        

computer_guess(10)
