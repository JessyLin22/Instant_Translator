#!/usr/bin/env python
# -*- coding:utf-8 -*-

# split sentense package
import jieba
from translate import Translator
from gtts import gTTS
import time
# play mp3 file package
import pygame
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

#Read audio
with sr.Microphone() as source:
    print("test...")
    r.adjust_for_ambient_noise(source,duration=5)
    print("say something!")
    # save the sound in audio by r.listen method.
    audio = r.listen(source)

try:
    print("Google Speech Recognition thinks you said:")
    # translate audio to text and set audio language = "zh-TW", you also can change any language you want to translate.
    print(r.recognize_google(audio,language="zh-TW"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("No response from Google Speech Recognition service:{0}".format(e))

# block the noted message.
jieba.setLogLevel(20)
# read text and set audio language = "zh-TW", you also can change any language you want to translate.
a = r.recognize_google(audio,language="zh-TW")
# split text to word.
b=jieba.cut(a,cut_all=False)
for words in b:
    print(words),"/",
print ("\n")

# you can set the language you want to translate.
translator= Translator(from_lang="chinese",to_lang="english")
translation = translator.translate(a)
print (translation)

# save as mp3 file , noted here i set en as translated language.
tts=gTTS(text=translation, lang="en")
# save the file on here and set the file name. you also can change the file path.
tts.save("C:\Python27\Test.mp3")

# read the mp3 file and play it.
# if you change path up, you should also change path here.
file = r"C:\Python27\Test.mp3"
pygame.mixer.init()
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.stop()
