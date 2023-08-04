# Adds names which then patients.py will check whether the person ur logging in as is a patient
# nameToAdd = input("What is your name to be registered under?")
# with open("patient_names.txt", "a") as file:
# file.write(nameToAdd + "\n")
import os
import random
import string

from faker import Faker
import Diseases

fake = Faker()


def get_random_age(min_age=18, max_age=90):
    return random.randint(min_age, max_age)



def sanitize_name(name):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_name = ''.join(c for c in name if c in valid_chars)
    return sanitized_name[:255]  # Truncate to allowable length for most file systems


for i in range(100):
    name = fake.name()
    age = get_random_age()
    disease = Diseases.getRandomDisease()
    status = Diseases.getRandomHealthStatus()

    folder_name = sanitize_name(name)

    # Create a new directory for each patient
    os.makedirs(f'patient_records/{folder_name}', exist_ok=True)

    # Create folder for age within patient folder
    os.makedirs(f"patient_records/{folder_name}/age", exist_ok=True)

    # Write the patient's data to a file in their directory
    with open(f'patient_records/{folder_name}/age/{age}', 'w') as file:
        file.write(f"Age: {age}")

    with open(f'patient_records/{folder_name}/{disease}', 'w') as file:
        file.write(f"Disease: {disease}\nStatus: {status}")


