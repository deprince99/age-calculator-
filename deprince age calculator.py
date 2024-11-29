
import datetime
date_of_birth = input("Insert your date of birth in this format (YYYY): ")
current_year = 2024
age = int(current_year) - int(date_of_birth)
print(str("You are " + str(age) + " years old."))



import datetime
date_of_birth = input("Insert your date of birth in this format (YYYY): ")
current_year = input("Insert current year in this format (YYYY): ")
age = int(current_year) - int(date_of_birth)
print(str("You are " + str(age) + " years old."))
