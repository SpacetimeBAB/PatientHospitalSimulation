import os
import random
import string
from faker import Faker
import Diseases
from nltk.corpus import names

fake = Faker()


def guess_gender(name):
    if name.title() in names.words('male.txt'):
        return 'Male'
    elif name.title() in names.words('female.txt'):
        return 'Female'
    else:
        return 'Unknown'


def get_random_age(min_age=18, max_age=90):
    return random.randint(min_age, max_age)


def sanitize_name(name):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_name = ''.join(c for c in name if c in valid_chars)
    return sanitized_name[:255]


for i in range(100):
    name = fake.name() # generate the full name
    firstName = name.split()[0] # get the first name from the split of full name
    age = get_random_age()
    disease = Diseases.getRandomDisease()
    status = Diseases.getRandomHealthStatus()
    gender = guess_gender(firstName) # use the firstName variable for gender prediction

    folder_name = sanitize_name(name) # use full name for folder naming

    os.makedirs(f'patient_records/{folder_name}', exist_ok=True)
    os.makedirs(f"patient_records/{folder_name}/age", exist_ok=True)

    with open(f'patient_records/{folder_name}/age/{age}', 'w') as file:
        file.write(f"Age: {age}")

    with open(f'patient_records/{folder_name}/{disease}', 'w') as file:
        file.write(f"Disease: {disease}\nStatus: {status}")

    with open(f"patient_records/{folder_name}/{gender}", "w") as file:
        file.write(f"Gender: {gender}\n")