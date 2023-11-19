import os

def search_files(directory, keyword):
    files_with_keyword = []

    for dirpath, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r') as file_content:
                if keyword in file_content.read():
                    files_with_keyword.append(filepath)

    return files_with_keyword

search_query = input("What are you looking for?")

# Use it like this
results = search_files('patient_records', search_query)
for file in results:
    print(file)

