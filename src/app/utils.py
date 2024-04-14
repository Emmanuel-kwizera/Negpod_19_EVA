def get_user_choice(message, valid_choices):
    choice = input(message)
    while choice not in valid_choices:
        choice = input("Invalid choice. Please try again: ")
    return choice


def get_meter_id(prompt):
    return input(prompt)
