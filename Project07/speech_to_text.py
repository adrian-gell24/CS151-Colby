
'''
speech_to_text.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: April 7, 2021
Date last modified: April 7, 2021

This file is a speech recognition library
'''




#import library

import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

def text_from_speech():

    result = ""

    # Reading Microphone as source

    # listening the speech and store in audio_text variable

    with sr.Microphone() as source:

        print("Talk")

        #r.adjust_for_ambient_noise(source)

        audio_text = r.listen(source)

        print("Time over, thanks")

   

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling  

        try:

            # using google speech recognition

            result = r.recognize_google(audio_text)

            print("Text: " + result)

        except:

            print("Sorry, I did not get that")

   

    return result