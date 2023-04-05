import json
from gui import QuizGUI

with open("questions.json") as file:
    content = file.read()

data = json.loads(content)

gui = QuizGUI(data)
gui.start()
