import json

with open("questions.json") as file:
    content = file.read()

data = json.loads(content)

while True:
    score = 0
    for question in data:
        print(question["Question_text"])
        for index, alternative in enumerate(question["alternatives"]):
            print(f"{index} - {alternative}")
        user_input = input("Enter the correct answer: ")
        try:
            user_input = int(user_input)
            if user_input < 0 or user_input >= len(question["alternatives"]):
                raise ValueError
        except ValueError:
            print("Enter a value that falls within the available options.")
            continue
        question["user_input"] = user_input
        # Here is the correction:
        if question["correct answer"] == question["user_input"]:
            print("You have entered the correct answer.")
            score += 1
        else:
            print("Please try the game again.")
    print(f"Your score is {score}/{len(data)}")
    continue_game = input("Do you want to continue the game? ")
    if continue_game.lower().startswith('y'):
        print("Ok, keep playing!")
    else:
        print("The game has ended.")
        break
