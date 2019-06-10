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

output_letters = []
def print_word(word, correct_guesses):
        for letter in word:
                if letter in correct_guesses:
                        output_letters.append(letter)
                else:
                        output_letters.append("_") 
                
        print(output_letters)
                
print_word(word, output_letters)



play_game()
 





# so now we need to create a function or if statement? for what level they choose