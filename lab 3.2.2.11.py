word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("input any word: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A" or letter =="E" or letter =="I" or letter =="O" or letter =="U":
        continue
    else:
        word_without_vowels = word_without_vowels + letter
print(word_without_vowels)