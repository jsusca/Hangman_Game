import random


def split(user_guess):
    return [char for char in user_guess]


hangman_status = {
    8: ("     _______    \n "
        "   |     __|    \n "
        "   |    (__)    \n "
        "   |            \n "
        "   |            \n "
        "   |            \n "
        "___|___            "),
    7: ("     _______    \n "
        "   |     __|    \n "
        "   |    (__)    \n "
        "   |      |     \n "
        "   |            \n "
        "   |            \n "
        "___|___            "),
    6: ("     _______    \n "
        "   |     __|    \n "
        "   |    (__)    \n "
        "   |   ___|     \n "
        "   |            \n "
        "   |            \n "
        "___|___            "),
    5: ("     _______    \n "
        "   |     __|    \n "
        "   |    (__)    \n "
        "   |   ___|___  \n "
        "   |            \n "
        "   |            \n "
        "___|___            "),
    4: ("     _______    \n "
        "   |     __|    \n "
        "   |    (__)    \n "
        "   |   ___|___  \n "
        "   |      |     \n "
        "   |            \n "
        "___|___            "),
    3: ("     _______    \n "
        "   |     __|    \n "
        "   |    (__)    \n "
        "   |   ___|___  \n "
        "   |      |     \n "
        "   |     /      \n "
        "___|___            "),
    2: ("     _______    \n "
        "   |     __|    \n "
        "   |    (__)    \n "
        "   |   ___|___  \n "
        "   |      |     \n "
        "   |     /      \n "
        "___|___ /          "),
    1: ("     _______    \n "
        "   |     __|    \n "
        "   |    (__)    \n "
        "   |   ___|___  \n "
        "   |      |     \n "
        "   |     / \\   \n "
        "___|___ /          ")
}


print("\nWelcome to a regular old game of Hangman!")

# Chooses random word from word_list.txt
word = random.choice(open("word_list.txt").read().split())
word2 = []
letters_guessed = []
guess_count = 9

hangman = ("     _______    \n "
           "   |       |    \n "
           "   |            \n "
           "   |            \n "
           "   |            \n "
           "   |            \n "
           "___|___            ")

print(hangman)

# Blank lines for each letter of chosen word
for i in word:
    word2.append("_ ")

print("\n" + "".join(word2))
print("\nRemaining guesses: 9")

# Show word for testing
# print("\n" + word)

# Loop until user wins or loses
while "".join(word2) != word and guess_count != 0:
    guess = input("Guess: ")

    if guess == "quit":
        break

    guess = split(guess)

    for x in range(0, len(guess)):
        if guess[x] in letters_guessed:
            print("You've already guessed that letter!\n")
            continue

        # If guess is correct, replace blank line with correct letter
        for i in range(0, len(word)):
            if guess[x] == word[i]:
                word2[i] = guess[x]

        # If guess is incorrect, deduct 1 from remaining guesses
        if guess[x] not in word:
            letters_guessed.append(guess[x])
            guess_count -= 1
            hangman = hangman_status.get(guess_count)

    # Print current word standing and remaining guesses
    print(hangman)
    print("\n" + "".join(word2))
    print("\nRemaining guesses:", guess_count, "  Letters guessed: ", ", ".join(letters_guessed))
    print("Type 'quit' to quit")

# win/loss message
if guess_count == 0 or guess == "quit":
    print("     _______    \n "
          "   |     __|    \n "
          "   |    (__)    \n "
          "   |   ___|___  \n "
          "   |      |     \n "
          "   |     / \\   \n "
          "___|___ /   \\     ")
    print("\nYou lose!")
    print("The word was", word)
else:
    print("\nCongratulations! You got it!")
