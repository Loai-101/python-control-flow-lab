# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.


def check_letter():
    # Your control flow logic goes here
    letter = input("Enter a letter: ").lower()
    if letter in "a, e, i, o, u":
        print(f"The letter {letter} is a vowel.")
    elif letter in "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z":
        print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid entry.")

check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.


def check_voting_eligibility():
    # Your control flow logic goes here
    age= int(input("Please enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    elif age < 0:
        print("Invalid entry.")
    else:
        print("You are not eligible to vote.")

check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.

def calculate_dog_years():
    age= int(input("Input a dog's age: "))
    if age <= 2:
        print(f"The dog's age in dog years is {age * 10}.")
    elif age > 2:
        print(f"The dog's age in dog years is {2 * 10 + (age - 2) * 7}.")
    elif age <= 0:
        print("No negative or 0 numbers allowed.")
    else:
        print("Invalid entry.")
  
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.


def weather_advice():
    cold= input("Is it cold? (yes/no): ").lower()
    raining= input("Is it raining? (yes/no): ").lower()
    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    elif cold == "no" and raining == "no":
        print("Wear light clothing.")
    else:
        print("Invalid entry.")
  
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.


def determine_season():
   month= input("Enter the month of the year (Jan - Dec): ")
   day= int(input("Enter the day of the month: "))
   if month in ["Dec", "Jan", "Feb"] and day >= 21:
       print(f"{month} {day} is in Winter.")
   elif month in ["Mar", "Apr", "May"] and day >= 20:
       print(f"{month} {day} is in Spring.")
   elif month in ["Jun", "Jul", "Aug"] and day >= 21:
       print(f"{month} {day} is in Summer.")
   elif month in ["Sep", "Oct", "Nov"] and day >= 22:
       print(f"{month} {day} is in Fall.")
   else:
       print("Invalid entry.")
       
determine_season()

#Level Up :

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.

def guess_number():
    target= 42
    for i in range(5):
        guess= int(input("Guess a number: "))
        if guess < target:
            print("Guess is too low.")
        elif guess > target:
            print("Guess is too high.")
        elif guess == target:
            print("Congratulations, you guessed correctly!")
            break
    else:
        print("Sorry, you failed to guess the number in five attempts.")

guess_number()

