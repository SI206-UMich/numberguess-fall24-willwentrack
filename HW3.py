# Your name: William Wentrack  123123123
# Your student id: 19194918
# Your email: wwentrac@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

# create a Digital Book of Answers



import random


class DigitalBookofAnswers():


    def __init__(self, answers):
        self.book_answer_list = answers  
        self.questions_asked_list = []
        self.answered_list = []  


 
    def __str__(self):

        if self.book_answer_list == []:
            return ""
        
        answer_str = ""
        for i in range(len(self.book_answer_list)):
            if i > 0:
                answer_str = answer_str + " - "
            answer_str = answer_str + self.book_answer_list[i]
        return answer_str


  
    def check_get_answer(self, question):
        
        for i in range(len(self.questions_asked_list)):
            if self.questions_asked_list[i] == question:
                question_asnwer = self.book_answer_list[self.answered_list[i]]
                return f"I've already answered this question. The answer is: {question_asnwer}"
            
        answer_index = random.randint(0, len(self.book_answer_list) - 1)
        self.answered_list.append(answer_index)
        self.questions_asked_list.append(question)
        question_answer = self.book_answer_list[answer_index]
        return question_answer


    # Creates open_book method
    # ARGUMENTS:
    #   self: the current object
    # RETURNS: None
    def open_book(self):
        times_turned = 1
        question = input(f"Turn {times_turned} - Please enter your question: ")
        if question == "Done":
            print("Goodbye! See you soon.")
            return
        else:
            print(self.check_get_answer(question))
            self.questions_asked_list.append(question)
            times_turned = len(self.questions_asked_list)
            



    # Create the answer_log method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a list
    def answer_log(self):

        pass


def test():
    answers_list = ['Believe in Yourself', 'Stay Open to the Future', 'Enjoy It']
    book = DigitalBookofAnswers(answers_list)

    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {book.answered_list}")
    print(f"Question History List: Expected: {[]}, Actual: {book.questions_asked_list}")
    print(" ")

    print("Test __str__:")
    expected = "Belive in Yourself - Stay Open to the Future - Enjoy It"
    print(f"Expected: {expected}, Actual: {str(book)}")
    print(" ")
    
    empty_book = DigitalBookofAnswers([])
    print("Test __str__: when it's an empty book without possible answers")
    expected = ""
    print(f"Expected: {expected}, Actual: {str(empty_book)}")
    print(" ")

    print("Testing return value of check_get_answer:")
    res = book.check_get_answer('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")

    print("Testing check_get_answer")
    book.book_answer_list = ['Go For It']
    res = book.check_get_answer('test question 2')
    print(f"Expected: {'Go For It'}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer adds answer index to answered_list:")
    book.book_answer_list = ['Go For It']
    book.answered_list = []
    book.check_get_answer('test question 2')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer does not add 'I've already answered this question' part to answered_list:")
    book.book_answer_list = ['Believe In Yourself']
    book.answered_list = [0]
    book.questions_asked_list = ['test question 3']
    book.check_get_answer('test question 3')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")


    print("Testing return value answer_log")
    book.book_answer_list = ['Follow Your Inner Voice', 'Stay Positive', 'Go For It']
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log())
    print(f"Expected: {list}, Actual: {res}")
    print(" ")

    print("Testing return value answer_log elements")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log()[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")

    print("Testing answer_log")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = book.answer_log()
    expected = ['3 - follow your inner voice', '2 - stay positive', '1 - go for it']
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing empty answer_log")
    book.answered_list = []
    res = book.answer_log()
    expected = []
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")



# Extra Credit
def my_test():
    # Put your test code here

    pass


def main():
    pass



# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    #main()
    test() 
    # my_test() #TODO: Uncomment if you do the extra credit
    