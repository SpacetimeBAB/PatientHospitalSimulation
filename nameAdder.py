# Adds names which then patients.py will check whether the person ur logging in as is a patient
# nameToAdd = input("What is your name to be registered under?")
# with open("patient_names.txt", "a") as file:
# file.write(nameToAdd + "\n")

import random
from faker import Faker
import Diseases

fake = Faker()


def get_random_age(min_age=18, max_age=90):
    return random.randint(min_age, max_age)

for i in range(100) :
    with open("patient_names.txt", "a") as file:
        file.write(fake.name() + ", ")
        file.write(str(get_random_age()) + ", ")
        file.write(Diseases.getRandomDisease() + "\n")




