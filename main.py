import json

filename = input("Enter JSON config file: ")

try:
    with open(filename, "r") as file:
        data = json.load(file)

    print("\nAvailable keys:")
    for key in data:
        print("-", key)

    search = input("\nEnter key to search: ")

    if search in data:
        print("Value:", data[search])
    else:
        print("Key not found.")

except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Invalid JSON format.")
