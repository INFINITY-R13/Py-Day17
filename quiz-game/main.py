# main.py

# Import necessary classes from other modules
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Create an empty list to hold the question objects
question_bank = []

# Loop through each question dictionary in the question_data list
for question in question_data:
    # Extract the question text and answer from the dictionary
    question_text = question['text']
    question_answer = question['answer']
    
    # Create a new Question object using the extracted text and answer
    new_question = Question(question_text, question_answer)
    
    # Add the newly created Question object to the question_bank list
    question_bank.append(new_question)

# Create a QuizBrain object, passing the list of question objects to it
quiz = QuizBrain(question_bank)

# Start a loop that continues as long as there are more questions in the quiz
while quiz.still_has_questions():
    # Get the next question and prompt the user for an answer
    quiz.next_question()

# Once the loop finishes, print a completion message and the final score
print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")