print("Hello welcome to the hospital")
nameOfPerson = input("What is your name?")
with open("patient_names.txt", "r") as file:
    patientNames = [line.strip() for line in file.readlines()]
    if nameOfPerson in patientNames:
        print("Hello " + nameOfPerson + ". Have a great stay here.")
    else:
        Register = input("It would appear you are not in the system. Would you like to register?").lower()

with open("patient_names.txt", "a") as file:
    if "yes" in Register:
        file.write(nameOfPerson + "\n")
    # else:
# print("Have a great day " + nameOfPerson + ".")
