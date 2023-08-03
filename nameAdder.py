# Adds names which then patients.py will check whether the person ur logging in as is a patient
nameToAdd = input("What is your name to be registered under?")
with open("patient_names.txt", "a") as file:
    file.write(nameToAdd + "\n")
