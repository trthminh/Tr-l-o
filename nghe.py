# import speech_recognition

# robot_ear = speech_recognition.Recognizer()
# with speech_recognition.Microphone() as mic: # mic = speech_recognition.Microphone()
# 	print("Robot: I'm Listening")
# 	audio = robot_ear.listen(mic)
	
# try:
# 	you = robot_ear.recognize_google(auodio)
# except:
# 	you = ""
# print("You: " + you)
import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic: 
# mic = speech_recognition.Microphone()
	print("Robot: I'm Listening...")
	# audio = robot_ear.listen(mic)
	audio = robot_ear.record(mic, duration = 2)
	# tang giam tieng on cho mic
	# robot_ear.adjust_for_ambient_noise(mic)
try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""
robot_mouth.say(you)
robot_mouth.runAndWait()
