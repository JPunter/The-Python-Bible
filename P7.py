#Pig latin translator
# converts words starting in a consonant by moving first consonant cluster to the end
# and adding 'ay', for example 'Cloud' would be come 'OudClay'
# converst words starting with a vowel by adding 'yay' to the end, for example
# Eat becomes Eatyay
#


#Get sentence from user

original = input("Please give me a sentence to translate to pig latin!: ").lower().strip()

#split sentence into words

words = original.split()

#loop through words and convert to pig latin

newWords = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        newWords.append(new_word)
    else:
        vowelPos = 0
        for letter in word:
            if letter not in "aeiou":
                vowelPos = vowelPos + 1
            else:
                break
        cons = word[:vowelPos]
        rest = word[vowelPos:]
        new_word = rest + cons + "ay"
        newWords.append(new_word)

#stick words back together

output = " ".join(newWords)

#output final sentence

print(output)

