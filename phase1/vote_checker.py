
birth_year = int(input("please enter ur birth year "))
current_year = 2026

your_age = current_year - birth_year

can_vote = your_age >= 18
is_senior = your_age >= 65

print(f"your are {your_age} years old ")
print(f"you can vote: {can_vote}")
print(f"you are senior: {is_senior}")
