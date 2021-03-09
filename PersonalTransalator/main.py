import playsound
import googletrans
import speech_recognition as recognise
import gtts
import random
import time

# to print all languages you can translate here
# print(googletrans.LANGUAGES)
# To detect the language in the message
# detector = googletrans.Translator().detect
# detected = detector(message)
# print("The code of this language is " + detected.lang + ". Confidence level is " + str(detected.confidence))


recognizer = recognise.Recognizer()
translator = googletrans.Translator()
print("Kindly please enter the input language as code [ eg:- 'en' 'en-US' 'ko'] ")
time.sleep(2.2)
input_lang = str(input("Please enter the input language [Def: en ] >  "))  # Change the Input Language
output_lang = str(input("Please enter the output language [Def: ko ] >  "))    # Change the Output language

if not input_lang:
    input_lang = 'en'

if not output_lang:
    output_lang = 'ko'
try:
    with recognise.Microphone() as listener:
        print("Start speaking")
        feeling = recognizer.listen(listener)
        words = recognizer.recognize_google(feeling, language=input_lang)
        print("This is what you spoke \n '" + words + "'")
except:
    pass

num = random.randint(0, 1000)
translated = translator.translate(words, dest=output_lang)
print("Translated text is '" + translated.text + "'")
translatedAudio = gtts.gTTS(translated.text, lang=output_lang)
file_name = "translated_voice" + str(num) + ".mp3"
translatedAudio.save(file_name)
playsound.playsound(file_name)
print("Sound file was saved as " + file_name)
