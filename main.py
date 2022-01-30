import speech_recognition
import os
import webbrowser


class function:
    def __init__(self, say, path):
        self.say = str("")
        self.paths = str("")


func = function("Прочитать файл", "C:/Users/feede/PycharmProjects/pythonProject5/todo.txt")
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def listen_me():
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language="ru-Ru").lower()
        return query


def open_file(txt):
    with open(txt[:-1]) as infp:
        data = infp.read()
    return data


def create_task(txt):
    print("Что добавим?")
    wr = listen_me()
    with open(txt[:-1], "a") as file:
        file.write("\n" + wr)
        print("Задача добавлена в todo.txt")


def china_clicker(query):
    print("Слушаю")

    for line in open('C:/Users/feede/PycharmProjects/pythonProject5/Options.txt', 'r'):
        if query == read_file_say(line, 0):
            if read_file_say(line, 1) == "0":
                webbrowser.open(read_file_say(line, 2), new=2)
                return "Открываю.."

            elif read_file_say(line, 1) == "1":
                create_task(read_file_say(line, 2))
                return ""

            elif read_file_say(line, 1) == "2":
                return open_file(read_file_say(line, 2))

            elif read_file_say(line, 1) == "3":
                os.system('shutdown -s')
                print("Работает")
                return ""


def read_file_say(line, num):
    say = line.split(" ")
    return say[num]
