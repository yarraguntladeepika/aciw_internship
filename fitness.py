class FitnessTracker:
    def __init__(self, filename="fitness_data.txt"):
        self.filename = filename

    def add_entry(self):
        date = input("Enter date (DD-MM-YYYY): ")
        steps = int(input("Enter steps walked: "))
        calories = int(input("Enter calories burned: "))
        workout = input("Enter workout type: ")

        with open(self.filename, "a") as f:
            f.write(f"{date},{steps},{calories},{workout}\n")

        print("✔ Data saved successfully!\n")

    def view_entries(self):
        try:
            with open(self.filename, "r") as f:
                data = f.readlines()
                if not data:
                    print("No fitness data found.\n")
                    return

                print("\nDate\t\tSteps\tCalories\tWorkout")
                print("-" * 50)
                for line in data:
                    date, steps, calories, workout = line.strip().split(",")
                    print(f"{date}\t{steps}\t{calories}\t\t{workout}")
                print()
        except FileNotFoundError:
            print("No data file found.\n")

    def summary(self):
        total_steps = 0
        total_calories = 0
        count = 0

        try:
            with open(self.filename, "r") as f:
                for line in f:
                    _, steps, calories, _ = line.strip().split(",")
                    total_steps += int(steps)
                    total_calories += int(calories)
                    count += 1

            if count > 0:
                print("\n--- Fitness Summary ---")
                print("Days tracked :", count)
                print("Total steps  :", total_steps)
                print("Total calories burned :", total_calories)
                print("Average steps/day :", total_steps // count)
                print()
            else:
                print("No data available.\n")

        except FileNotFoundError:
            print("No data file found.\n")


tracker = FitnessTracker()

while True:
    print("=== Personal Fitness Tracker ===")
    print("1. Add daily fitness data")
    print("2. View all fitness data")
    print("3. View summary")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        tracker.add_entry()
    elif choice == "2":
        tracker.view_entries()
    elif choice == "3":
        tracker.summary()
    elif choice == "4":
        print("Thank you! Stay fit 💪")
        break
    else:
        print("Invalid choice. Try again.\n")