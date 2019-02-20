from random import choice

questions = [
    "Why does the internet work?: ",
    "Why is the sky blue?: ",
    "Why is grandma old?: "
    ]


question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("But why?: ").strip().lower()

print("Oh, OK")
