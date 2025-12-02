class QuizBrain:
    
    def __init__(self,q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0
    
    def still_has_question(self):
        return self.question_num < len(self.question_list)
           

    def next_question(self):
            current_qn = self.question_list[self.question_num]
            self.question_num += 1
            s = input(f"Q.{self.question_num}: {current_qn.text}.(True/False)?:").lower()
            self.check_answer(s,current_qn.answer)
    def check_answer(self,user_answer,correct_answer):
            if user_answer.lower() == correct_answer.lower():
                print("you got it the correct answer!")
                self.score += 1
                
            else:
                print("sorry..thats Wrong!")
            print(f"The correct answer is {correct_answer}")
            print(f"your current score is {self.score}/{self.question_num}")
            print()
           
            
            