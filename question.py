# Define a function to ask a question and get user input
def ask_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter the number of your answer: ")
    try:
        user_answer = int(user_answer) - 1
        if user_answer == question_data["correct"]:
            print("Correct!")
            return True
        else:
            print(f"Sorry, the correct answer is {question_data['options'][question_data['correct']]}")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return ask_question(question_data)