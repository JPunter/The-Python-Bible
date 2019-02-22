vowel = 0
consonant = 0

word = input("Please select a word for testing: ")

for letter in word:
    if letter.lower() in "aeiou":
        vowel = vowel + 1
    elif letter == " ":
        pass
    else:
        consonant = consonant + 1

print("The number of vowels in your word is {}".format(vowel))
print("The number of consonants is {}".format(consonant))
