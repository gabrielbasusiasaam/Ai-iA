import win32com.client as wincl

class Say(x):
	speak = wincl.Dispatch("SAPI.SpVoice")
	speak.Speak(x)
