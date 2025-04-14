class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options  # Dictionary: {'A': 'Option 1', ...}
        self.correct_option = correct_option

    def is_correct(self, selected_option):
        return selected_option == self.correct_option
