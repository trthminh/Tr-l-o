import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""

i = 0

while True:
	if i == 10:
		robot_brain = "If you don't say, then Bye Minh"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	# Nghe
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
	print("You: " + you)

	# Hieu


	if you == "":
		robot_brain = "I can't hear you, try again"
		i = i + 1
	elif "hello" in you:
		robot_brain = "Hello Minh"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain = "Bye Minh, see you again"
		print("Robot: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else: robot_brain = "I'm fine thank you"

	# Noi

 	# robot_brain = "You are very intelligent!"
	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()