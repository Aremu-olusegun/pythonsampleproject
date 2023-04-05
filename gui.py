import PySimpleGUI as sg

class QuizGUI:
    def __init__(self, data):
        self.data = data
        self.score = 0
        self.index = 0

    def start(self):
        layout = [[sg.Text("Welcome to the Quiz Game!")],
                  [sg.Text("Press the 'Start' button to begin.")],
                  [sg.Button("Start"), sg.Button("Exit")]]

        self.window = sg.Window("Quiz Game", layout)

        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "Start":
                self.show_question()

        self.window.close()

    def show_question(self):
        question = self.data[self.index]
        question_layout = [[sg.Text(question["Question_text"])],
                           [sg.Text("Select the correct answer:")]]
        for index, alternative in enumerate(question["alternatives"]):
            question_layout.append([sg.Radio(alternative, group_id="answer", key=index)])
        question_layout.append([sg.Button("Submit")])
        self.question_window = sg.Window("Question", question_layout)

        while True:
            event, values = self.question_window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Submit":
                user_input = None
                for index, alternative in enumerate(question["alternatives"]):
                    if values[index]:
                        user_input = index
                        break
                if user_input is None:
                    sg.popup("Please select an answer.", title="Error")
                else:
                    question["user_input"] = user_input
                    if question["correct answer"] == question["user_input"]:
                        sg.popup("You have entered the correct answer.", title="Correct")
                        self.score += 1
                    else:
                        sg.popup("Please try the game again.", title="Incorrect")
                    self.index += 1
                    if self.index == len(self.data):
                        sg.popup(f"Your score is {self.score}/{len(self.data)}", title="Game Over")
                        self.window.close()
                        break
                    else:
                        self.question_window.close()
                        self.show_question()
                break

        self.question_window.close()
