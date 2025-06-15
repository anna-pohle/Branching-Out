import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    if len(filtered_users) == 0:
        print("No users found")
    else:
        for user in filtered_users:
            print(user)

def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    if len(filtered_users) == 0:
        print("No users found")
    else:
        for user in filtered_users:
            print(user)

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    if len(filtered_users) == 0:
        print("No users found")
    else:
        for user in filtered_users:
            print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        while True:
            age_to_search = input("Enter an age to filter users by: ")
            try:
                age_to_search = int(age_to_search)
            except ValueError:
                print("Please enter a number")
            filter_users_by_age(age_to_search)
            break

    elif filter_option == "email":
        while True:
            email_to_search = input("Enter an email-address to filter users by: ")
            if not "@" in email_to_search:
                print ("The email address must be in the format xx@xx.xx \n (x is indicating the minimum amount of characters in each section")
            elif not "." in email_to_search:
                print("The email address must be in the format xx@xx.xx \n (x is indicating the minimum amount of characters in each section")
            elif len(email_to_search.split("@")[0]) < 2:
                print ("the name before the '@' must be at least two characters long.")
            elif len(email_to_search.split("@")[1].split('.')[0]) < 2:
                print ("the domain after the '@' must be at least two characters long.")
            elif len(email_to_search.split(".")[1]) < 2:
                print ("the ending after the '.' must be at least two characters long.")
            else:
                filter_users_by_email(email_to_search)
                break
    else:
        print("Filtering by that option is not yet supported.")
