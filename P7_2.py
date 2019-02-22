original = input("Please give me a sentence: ").lower().strip()

words = original.split()

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
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
        new_words.append(new_word)

output = " ".join(new_words)
print(output)
