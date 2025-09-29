# quiz_brain.py

class QuizBrain:
    """Manages the quiz logic, including tracking questions, score, and user answers."""

    def __init__(self, q_list):
        """
        Initializes the QuizBrain object.
        :param q_list: A list of Question objects.
        """
        # The current question number (starts at 0 for list indexing)
        self.question_number = 0
        # The user's current score
        self.score = 0
        # The list of all question objects for the quiz
        self.question_list = q_list

    def still_has_questions(self):
        """
        Checks if there are more questions left in the quiz.
        :return: True if there are remaining questions, False otherwise.
        """
        # Returns True if the current question number is less than the total number of questions
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question, prompts the user, and checks their answer.
        """
        # Get the current question object from the list using the question_number as the index
        current_question = self.question_list[self.question_number]
        
        # Increment the question number for the next question
        self.question_number += 1
        
        # Prompt the user with the current question number and text
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        
        # Check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Compares the user's answer to the correct answer and updates the score.
        :param user_answer: The answer provided by the user.
        :param correct_answer: The correct answer from the question object.
        """
        # Compare the user's answer (in lowercase) with the correct answer (in lowercase)
        if user_answer.lower() == correct_answer.lower():
            # If correct, increment the score and provide positive feedback
            self.score += 1
            print("That's Right!")
        else:
            # If incorrect, provide feedback that the answer was wrong
            print("That's Wrong.")
            
        # Always show the correct answer
        print(f"The correct answer was: {correct_answer}.")
        # Show the user's current score
        print(f"Your current score is: {self.score}/{self.question_number}")
        # Print a newline for better readability between questions
        print("\n")