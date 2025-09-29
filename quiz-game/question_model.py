# question_model.py

class Question:
    """Models a single question with a text and an answer."""
    
    def __init__(self, q_text, q_answer):
        """
        Initializes a Question object.
        :param q_text: The text of the question (str).
        :param q_answer: The answer to the question (str, typically "True" or "False").
        """
        self.text = q_text
        self.answer = q_answer