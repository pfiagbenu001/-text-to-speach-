import pyttsx3
import PySimpleGUI as sg

# Define the layout of the GUI
layout = [
    [ sg.InputText(key="text_input"),sg.Button("Speak", bind_return_key=True)],
    [sg.Text("Select voice type:"), sg.Radio("Male", "voice", default=True, key="male"), sg.Radio("Female", "voice", key="female")],


]

# Create the GUI window
window = sg.Window("Text-to-Speech", layout)

# Create a text-to-speech engine
engine = pyttsx3.init()

# Define the speak function
def speak(text):


    # Say the text
    engine.say(text)
    engine.runAndWait()

# Handle events in the GUI
while True:
    event, values = window.read()
    if event in (None, "Cancel"):
        break
    elif event == "Speak":
        text_input = values["text_input"]
        speak(text_input)

# Close the GUI window and the text-to-speech engine
window.close()
engine.stop()
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
