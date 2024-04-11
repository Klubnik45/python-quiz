from input_validation import load_json
import os #библиотека операционной системы
import json
global total_points

def save_game(file_name, level, points, total_points):
    with open(f"{file_name}.json","w") as file:
        json.dump({"level":level, "user_points":points+total_points},file)


def check_answer(answer):
    global total_points
    if answer==str(level_data["questions"][q]["correct"]):
        total_points+=level_data["points"]
        print("Well-done")
    else:
        print("Better luck next time.")
   

def load_user_data(file_name):
    if os.path.isfile(f"{file_name}.json"):
        print("File exists")
        with open("save.json","r") as file:
            data=load_json("save")
            level=data["level"]
            user_points=data["user_points"]
    else:
        level=1
        user_points=0
        print("File not found")
    
    return (level, user_points)


def display_result(level):
    global total_points
    max_points=len(level_data["questions"])*level_data["points"]*0.7
    if total_points>=max_points:
        level+=1
        print("You got new level!")
    else:
        print("You lose!")
    print(f"All points = {total_points}")
    return level


def game_over(level):
    if level>7:
        return True
    else:
        return False
    

user_input=input("Do you want to play?, Y/N\n").upper()

while user_input=="Y":
    total_points=0
    level, user_points=load_user_data("save")
    
    if game_over(level):
        print(f'Game over! {load_json("data")[f"level_{7}"]["rank"]}')
        break
    else:
        level_data=load_json("data")[f"level_{level}"]
    
    print(f'LEVEL # {level_data["level"]}')
    for q in range(len(level_data["questions"])):
        print(f'{q+1}. {level_data["questions"][q]["question"]}')
        print("Choose one answer: ")
        
        for a in range(len(level_data["questions"][q]["answers"])):
            print(f'{a+1}. {level_data["questions"][q]["answers"][a]}')
        
        user_answer=input("Your answer: \n")
   
        check_answer(user_answer)
          
    level=display_result(level)
    save_game("save", level, user_points, total_points)
    user_input=input("Do you want to play?, Y/N\n").upper()