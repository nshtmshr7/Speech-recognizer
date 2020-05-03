#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition


# In[9]:


import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")


# In[ ]:




