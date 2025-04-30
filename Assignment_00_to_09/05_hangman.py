import random

words = [
    'python', 'hangman', 'keyboard', 'mouse', 'laptop', 'monitor',
    'developer', 'function', 'variable', 'internet', 'project', 'github',
    'programming', 'terminal', 'language', 'debugging', 'compiler', 'software'
]

word = random.choice(words)
guessed = set()
lives = 6

print("🎯 Welcome to Hangman!")

while lives > 0:
    display = [letter if letter in guessed else '-' for letter in word]
    print("Word:", ' '.join(display))

    if '-' not in display:
        print("🎉 You guessed it! The word was:", word)
        break

    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single letter (a-z).")
        continue
    if guess in guessed:
        print("⚠️ Already guessed!")
    elif guess in word:
        guessed.add(guess)
        print("✅ Correct!")
    else:
        guessed.add(guess)
        lives -= 1
        print("❌ Wrong! Lives left:", lives)

if lives == 0:
    print("You lost! The word was:", word)