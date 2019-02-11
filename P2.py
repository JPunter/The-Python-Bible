# Ask user for name

name = input("What is your name?: ")

# Ask user for age

age = input("What is your age?: ")

# Ask user for city

city = input("What city do you live in?: ")

# Ask user what they enjoy

hobby = input("What is your favourite hobby?: ")

# Create output text

conc = "Hello {}! You are {} years old and you live in {}. Your favourite hobby is {}"
output = conc.format(name, age, city, hobby)

# Print output to screen

print(output)
