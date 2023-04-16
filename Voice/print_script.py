import speech_recognition as sr
import os

# initialize the recognizer
r = sr.Recognizer()


# define the function that will run the script
def run_script():
    os.system("python3 script_to_run.py")

# define the function that listens for the command
def listen_for_command():
    while True:
        with sr.Microphone() as source:
            print("Say 'print' to run the script")
            audio = r.listen(source)

            try:
                command = r.recognize_google(audio)
                if command == "print":
                    run_script()
                    print("Script executed successfully")
                else:
                    print("Command not recognized")
            except:
                print("Could not understand audio")

# call the function to listen for the command
listen_for_command()
