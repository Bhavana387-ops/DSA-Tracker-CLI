import json
import os

FILE = "dsa_problems.json"

def load_problems():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r') as f:
        return json.load(f)

def save_problems(problems):
    with open(FILE, 'w') as f:
        json.dump(problems, f, indent=4)

def add_problem():
    title = input("Enter problem title: ")
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ")
    topic = input("Enter topic (Array, Tree, etc.): ")
    status = input("Status (Solved/Unsolved): ")
    problems = load_problems()
    problems.append({
        "title": title,
        "difficulty": difficulty.capitalize(),
        "topic": topic.capitalize(),
        "status": status.capitalize()
    })
    save_problems(problems)
    print("✅ Problem added!")

def view_problems():
    problems = load_problems()
    if not problems:
        print("No problems added yet.")
        return
    for i, p in enumerate(problems, start=1):
        print(f"{i}. {p['title']} - {p['difficulty']} - {p['topic']} - {p['status']}")

def filter_by_difficulty():
    diff = input("Filter by difficulty (Easy/Medium/Hard): ").capitalize()
    problems = [p for p in load_problems() if p["difficulty"] == diff]
    for i, p in enumerate(problems, start=1):
        print(f"{i}. {p['title']} - {p['topic']} - {p['status']}")

def main():
    while True:
        print("\n📌 DSA Tracker Menu:")
        print("1. Add Problem")
        print("2. View All Problems")
        print("3. Filter by Difficulty")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_problem()
        elif choice == '2':
            view_problems()
        elif choice == '3':
            filter_by_difficulty()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
