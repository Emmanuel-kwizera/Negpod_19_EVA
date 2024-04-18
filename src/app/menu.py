class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        print("\n", self.title)
        for i, option in enumerate(self.options, start=1):
            print(f"{option}")

    def get_user_choice(self):
        while True:
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and", len(self.options))
            except ValueError:
                print("Invalid choice. Please enter a number.")
