from quiz import Quiz


user_input = "Y"
while user_input == "Y":
    quiz = Quiz("save")
    tasks = quiz.get_tasks()

    for task in tasks:
        print(task["q"])
        print(task["answers"])
        quiz.check_answer(input("Your answer? "), task["correct"])
    
    quiz.display_result()
    quiz.save_game()

    user_input = input("Do you want to continue play? \n Y/N").upper()
    
    if quiz.game_over():
        user_input = input("You beat all levels. Do you want to reset the game?").upper()
        if user_input == "Y":
            quiz.reset()
        else:
            print("Congratulations!!!")
    