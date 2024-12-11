import gtts
import playsound
text=input("Enter something here:")
sound=gtts.gTTS(text,lang='hi') #en for english mr for marathi
sound.save("newsound.mp3")
playsound.playsound("newsound.mp3")
