<<<<<<< HEAD
# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("input any word: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A" or letter =="E" or letter =="I" or letter =="O" or letter =="U":
        continue
    else:
=======
# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("input any word: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A" or letter =="E" or letter =="I" or letter =="O" or letter =="U":
        continue
    else:
>>>>>>> a6b3300a7216cd1a804b7ddc0ef7b23f249ded6b
        print(letter)