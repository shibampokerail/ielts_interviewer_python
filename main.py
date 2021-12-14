import pyttsx3
import time
import random
from speaking_questions import p1_questions, p2_questions, p3_questions


class Speaker:
    def __init__(self, default_name="Eve"):
        self.name = default_name
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 165)

    def speak(self, text, pause_time=0.5):
        self.engine.say(text)
        self.engine.runAndWait()
        time.sleep(pause_time)

    def give_introduction(self):
        self.speak(f"Hello, my name is {self.name}, and welcome to I elts speaking mock test")

    def listen(self):
        listening_vioces = ["m hmm", "yes"]
        self.engine.say("yes")
        self.engine.runAndWait()

    def ask_questions_part_one(self, questions_list):
        self.speak("Okay, In part one, I'm going to ask you some personal questions.")
        question = random.choice(questions_list)
        for i in question['questions']:
            self.speak(i, 15)
        self.speak("Okay, Thank you.")

    def ask_questions_part_2(self, questions_list):
        self.speak("Now, In part two, you will have to talk about a topic for one to two minutes.")
        self.speak("You can make some notes if you wish.")
        self.speak("Here is your topic.")
        question = random.choice(questions_list)
        print(question)
        self.speak("Your one minute to prepare starts now.")
        time.sleep(60)
        self.speak("Your time is up.")
        self.speak("Please start speaking now.")
        time.sleep(120)
        self.speak("Your time is up. Thank You")

    def ask_questions_part_3(self, questions_list):
        self.speak("Now, In part three, I will ask you some more general questions.")
        question = random.choice(questions_list)
        for i in question['questions']:
            self.speak(i, 45)

    def end_test(self):
        self.speak("Okay, Thank You. This is the end of speaking test.")



def take_speaking_test():
    Eve = Speaker()

    Eve.give_introduction()

    Eve.speak("Could you please tell me your full name", 3)

    Eve.speak("So what should I call you", 2)

    Eve.ask_questions_part_one(p1_questions)

    Eve.ask_questions_part_2(p2_questions)

    Eve.ask_questions_part_3(p3_questions)

    Eve.end_test()


take_speaking_test()
