from datetime import date


def main():
    while True:
        birthday_input = input("Enter your birthday (YYYY-MM-DD): ").strip()

        try:
            birth_date = date.fromisoformat(birthday_input)
            break
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

    today = date.today()

    if birth_date > today:
        print("Birthday cannot be in the future.")
        return

    age_in_days = (today - birth_date).days
    print(f"You are {age_in_days} days old.")


if __name__ == "__main__":
    main()

