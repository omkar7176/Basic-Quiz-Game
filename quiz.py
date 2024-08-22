# Import the quiz data and question function
from quiz_data import quiz_data
from question import ask_question

def run_quiz():
    # Initialize score
    score = 0

    # Ask each question and update the score
    for question in quiz_data:
        if ask_question(question):
            score += 1

    # Display the final score
    print(f"Your final score is {score} out of {len(quiz_data)}")

if __name__ == "__main__":
    run_quiz()