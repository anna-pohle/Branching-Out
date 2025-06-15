import json

def filter_option_choice(users):
    while True:
        filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' are supported): ").strip().lower()
        print("")
        if filter_option == "name":
            filtered_users = filter_users_by_name(users)
            return filtered_users
        elif filter_option == "age":
            filtered_users = filter_users_by_age(users)
            return filtered_users
        elif filter_option == "email":
            filtered_users = filter_users_by_email(users)
            return filtered_users
        else:
            print("Filtering by that option is not yet supported.")


def filter_users_by_name(users):
    name_to_search = (input("Enter a name to filter users: ").strip())

    users_by_name = [user for user in users if user["name"].lower() == name_to_search.lower()]
    return users_by_name

def filter_users_by_age(users):
    while True:
        age_to_search = input("Enter an age to filter users by: ")
        try:
            age_to_search = int(age_to_search)
            break
        except ValueError:
            print("Please enter a whole number.")

    users_by_age = [user for user in users if user["age"] == age_to_search]
    return users_by_age


def filter_users_by_email(users):
    while True:
        email_to_search = input("Enter an email-address to filter users by: ")
        if not "@" in email_to_search:
            print(
                "The email address must be in the format xx@xx.xx \n (x is indicating the minimum amount of characters in each section")
        elif not "." in email_to_search:
            print(
                "The email address must be in the format xx@xx.xx \n (x is indicating the minimum amount of characters in each section")
        elif len(email_to_search.split("@")[0]) < 2:
            print("the name before the '@' must be at least two characters long.")
        elif len(email_to_search.split("@")[1].split('.')[0]) < 2:
            print("the domain after the '@' must be at least two characters long.")
        elif len(email_to_search.split(".")[1]) < 2:
            print("the ending after the '.' must be at least two characters long.")
        else:
            users_by_mail = [user for user in users if user["email"].lower() == email_to_search.lower()]
            return users_by_mail


def main():
    with open("users.json", "r") as file:
        users = json.load(file)

    while True:
        filtered_users = filter_option_choice(users)

        if len(filtered_users) == 0:
            print("No users found")
            print("")
        else:
            for user in filtered_users:
                print(user)
            print("")

        wish_to_continue = input("would you like to filter again? (y/n)")
        if "n" in wish_to_continue:
            print("Goodbye!")
            break
        else:
            continue


if __name__ == "__main__":
    main()
