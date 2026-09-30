# Python Quiz Game

score = 0


def ask_question(question, options, answer):
    global score

    print("\n" + question)

    for option in options:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == answer:
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong answer!")


def show_result():
    print("\n==============================")
    print("          QUIZ RESULT")
    print("==============================")

    print("Your Score:", score, "/ 10")

    percentage = (score / 10) * 100

    print("Percentage:", percentage, "%")

    if score == 10:
        print("Excellent! 🏆")
    elif score >= 7:
        print("Very Good! 👏")
    elif score >= 5:
        print("Good! 👍")
    else:
        print("Keep practicing! 📚")


def start_quiz():
    global score

    score = 0

    print("\n==============================")
    print("       PYTHON QUIZ GAME")
    print("==============================")

    questions = [

        (
            "1. Which language are we using?",
            ["A. Java", "B. Python", "C. C++", "D. HTML"],
            "B"
        ),

        (
            "2. Which symbol is used for comments in Python?",
            ["A. //", "B. <!-- -->", "C. #", "D. **"],
            "C"
        ),

        (
            "3. Which function is used to display output?",
            ["A. input()", "B. print()", "C. display()", "D. output()"],
            "B"
        ),

        (
            "4. Which data type stores True or False?",
            ["A. String", "B. Integer", "C. Boolean", "D. Float"],
            "C"
        ),

        (
            "5. Which symbol is used for multiplication?",
            ["A. +", "B. -", "C. /", "D. *"],
            "D"
        ),

        (
            "6. Which keyword is used to create a function?",
            ["A. function", "B. def", "C. fun", "D. create"],
            "B"
        ),

        (
            "7. Which one is a Python loop?",
            ["A. for", "B. repeat", "C. loop", "D. iterate"],
            "A"
        ),

        (
            "8. Which data structure uses []?",
            ["A. Tuple", "B. List", "C. Dictionary", "D. Set"],
            "B"
        ),

        (
            "9. What is 10 + 20?",
            ["A. 20", "B. 25", "C. 30", "D. 40"],
            "C"
        ),

        (
            "10. Which function gets input from the user?",
            ["A. scan()", "B. get()", "C. input()", "D. read()"],
            "C"
        )
    ]

    for question, options, answer in questions:
        ask_question(question, options, answer)

    show_result()


def main():
    while True:

        print("\n==============================")
        print("       MAIN MENU")
        print("==============================")
        print("1. Start Quiz")
        print("2. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_quiz()

        elif choice == "2":
            print("Thanks for playing! 👋")
            break

        else:
            print("Invalid choice. Try again.")


main()
