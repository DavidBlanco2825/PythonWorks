import random
import hangman_art
import hangman_words


print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}. And it haves {word_length} letters.')

display = []
for i in range(0, word_length):
    display.append("_")

user_lives = 6
end_of_the_game = False

while not end_of_the_game:

    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f'You already guessed the letter "{guess}", don\'t be a dummy.')
    i = 0
    for n in range(0, word_length):
        if guess == chosen_word[n]:
            i += 1
            display[i - 1] = guess
        else:
            i += 1

    if guess not in chosen_word:
        user_lives -= 1
        print(f'The letter "{guess}" is not in the word.\nYou lose a live. Live count: {user_lives}')
        if user_lives == 0:
            end_of_the_game = True
            print("You Lose")
    if "_" not in display:
        end_of_the_game = True
        print("You win!")

    print(hangman_art.stages[user_lives])

