import json
import os
from input_validation import load_json

class Quiz():
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__total_points = 0
        self.__level, self.__user_points = self.load_user_data()
        self.__level_data = load_json("data")[f"level_{self.__level}"]


    def get_file_name(self):
        return self.__file_name
    

    def get_total_points(self):
        return self.__total_points


    def get_level(self):
        return self.__level


    def get_user_points(self):
        return self.__user_points
    

    def get_level_data(self):
        return self.__level_data
    

    def  set_file_name(self, file_name):
        self.__file_name = file_name


    def save_game(self):
        with open(f"{self.__file_name}.json","w") as file:
            json.dump({"level":self.__level, "user_points":self.__user_points+self.__total_points},file)


    
    def load_user_data(self):
        if os.path.isfile(f"{self.__file_name}.json"):
            print("File exists")
            with open("save.json","r") as file:
                data=load_json("save")
                level=data["level"]
                user_points=data["user_points"]
                if level > 7:
                    level = 7
        else:
            level=1
            user_points=0
            print("File not found")
        return (level, user_points)    
    
        
    def check_answer(self, answer, correct):

        if str(answer).strip().lower().replace(" ", "") == str(correct).strip().lower().replace(" ",""):
            self.__total_points+=self.__level_data["points"]
            print("Well-done")
        else:
            print("Better luck next time.")


    def display_result(self):
        max_points = len(self.__level_data["questions"])*self.__level_data["points"]*0.7
        if self.__total_points >= max_points:
            self.__level += 1
            print("You got new level!")
        else:
            print("You lose!")
        print(f"All points = {self.__total_points}")
            

    def game_over(self):
        if self.__level > 7:
            return True
        else:
            return False


    def game_over_massage(self):
        if self.game_over(self.__level):
            return f'Game over! {load_json("data")[f"level_{7}"]["rank"]}'
        

    def get_tasks(self):
        tasks = []
        for q in range(len(self.__level_data["questions"])):
            new_dict = {}
            new_dict["q"] = self.__level_data["questions"][q]["question"]
            new_dict["answers"] = []

            for a in range(len(self.__level_data["questions"][q]["answers"])):
                new_dict["answers"].append(self.__level_data["questions"][q]["answers"][a])
            new_dict["correct"] =  self.__level_data["questions"][q]["correct"]
            tasks.append(new_dict)
        return tasks
    

    def reset(self):
        self.__level = 1
        self.__total_points = 0
        self.__user_points = 0
        self.save_game()
        

#new_quiz = Quiz("save")

#print(new_quiz.get_total_points(), new_quiz.get_user_points(), new_quiz.get_level())
#print(new_quiz.get_tasks())