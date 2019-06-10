word = "beach"

def user_guess(correct_guesses, incorrect_guesses):
    guess = input("Please guess a letter to see if it's in your word: ")

    if guess in word:
        correct_guesses.append(guess)
        print(guess + " is Correct!")
        print(correct_guesses)
    else:
        incorrect_guesses.append(guess)
        print(guess + " is Incorrect")
        print(incorrect_guesses)

def play_game():   
    correct_guesses = []
    incorrect_guesses = []
    while True: 
        user_guess(correct_guesses, incorrect_guesses)


play_game()
 





# so now we need to create a function or if statement? for what level they choose