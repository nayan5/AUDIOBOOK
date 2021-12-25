# AUDIOBOOK from PDF

import pyttsx3                              #pyttsx3 is a text-to-speech conversion library in Python
import PyPDF2                               #PyPDF2 is a pure-python PDF library capable of splitting, merging together, cropping, and transforming the pages of PDF files
from tkinter.filedialog import *
book = askopenfilename()                    #take file name from ur device

pdfreader = PyPDF2.PdfFileReader(book) 
pages = pdfreader.numPages                  #return pagenumber

for num in range(0,pages):                  #read all data from all pages
    page = pdfreader.getPage(num)
    text = page.extractText()               #extract text
    player = pyttsx3.init()                 #text-to-speech-object = player
    player.say(text)          
    player.runAndWait()

# AUDIOBOOK from PDF --> This Program Reads all content of the PDF out loud.