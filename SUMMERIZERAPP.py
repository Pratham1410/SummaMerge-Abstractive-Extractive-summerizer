import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from unittest import result






import pyttsx3
import pyaudio


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# NLP Pkgs
import re


from spacy_summarization import text_summarizer
from nltk_summarization import nltk_summarizer
from abstractive_summarization import abstractive_summarizer

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Structure and Layout
window = Tk()
window.title("")
window.geometry("1800x1800")
window.config(background='BLACK')

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn', )

# TAB LAYOUT
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"File":^20s}')
tab_control.add(tab3, text=f'{"URL":^20s}')
tab_control.add(tab4, text=f'{"Comparer ":^20s}')


label1 = Label(tab1, text='Summaryzer', padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text='File Processing', padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text='URL', padx=5, pady=5)
label3.grid(column=0, row=0)

label3 = Label(tab4, text='Compare Summarizers', padx=5, pady=5)
label3.grid(column=0, row=0)



tab_control.pack(expand=1, fill='both')


# Functions
def get_summary():
    raw_text = str(entry.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = '\nSummary:{}'.format(final_text)
    tab1_display.insert(tk.END, result)

def nltk_summary():
    raw_text = str(entry.get('1.0', tk.END))
    final_text = nltk_summarizer(raw_text)
    print(final_text)
    result = '\nSummary:{}'.format(final_text)
    tab1_display.insert(tk.END, result)

def get_abstractivesummary():
    raw_text = str(entry.get('1.0', tk.END))
    final_text = abstractive_summarizer(raw_text)
    print(final_text)
    result = '\nSummary:{}'.format(final_text)
    tab1_display.insert(tk.END, result)

def speak_summary():
    raw_text = str(entry.get('1.0', tk.END))
    final_text = abstractive_summarizer(raw_text)
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', 150)  
    speak(final_text)





# Clear entry widget
def clear_text():
    entry.delete('1.0', END)


def clear_display_result():
    tab1_display.delete('1.0', END)


# Clear Text  with position 1.0
def clear_text_file():
    displayed_file.delete('1.0', END)


# Clear Result of Functions
def clear_text_result():
    tab2_display_text.delete('1.0', END)


# Clear For URL
def clear_url_entry():
    url_entry.delete(0, END)


def clear_url_display():
    tab3_display_text.delete('1.0', END)


# Clear entry widget
def clear_compare_text():
    entry1.delete('1.0', END)


def clear_compare_display_result():
    tab4_display.delete('1.0', END)


# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
    file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files", ".txt"), ("All files", "*")))
    read_text = open(file1).read()
    displayed_file.insert(tk.END, read_text)


def get_file_summary():
    raw_text = displayed_file.get('1.0', tk.END)
    final_text = text_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab2_display_text.insert(tk.END, result)

def get_file_abstractivesummary():
    raw_text = displayed_file.get('1.0', tk.END)
    final_text = abstractive_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab2_display_text.insert(tk.END, result)

def speak_filesummary():
    speak(result)
    tab1_display.insert(tk.END)


# Fetch Text From Url
def get_text():
    raw_text = str(url_entry.get())
    page = urlopen(raw_text)
    soup = BeautifulSoup(page)
    fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    url_display.insert(tk.END, fetched_text)


def get_url_summary():
    raw_text = url_display.get('1.0', tk.END)
    final_text = text_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab3_display_text.insert(tk.END, result)

def get_url_abstractivesummary():
    raw_text = url_display.get('1.0', tk.END)
    final_text = abstractive_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab3_display_text.insert(tk.END, result)

def speak_urlsummary():
   raw_text = url_display.get('1.0', tk.END)
   final_text = abstractive_summarizer(raw_text)
   speak(final_text)
   tab1_display.insert(tk.END)


# COMPARER FUNCTIONS

def use_spacy():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = '\nSpacy Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_nltk():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = nltk_summarizer(raw_text)
    print(final_text)
    result = '\nNLTK Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)

def use_abstractive():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = abstractive_summarizer(raw_text)
    print(final_text)
    result = '\nAbstractive Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)



def speak_comparesummary():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = abstractive_summarizer(raw_text)
    
    speak(final_text)
    tab1_display.insert(tk.END)


# MAIN NLP TAB
l1 = Label(tab1, text="Enter Text To Summarize")
l1.grid(row=1, column=0)

entry = Text(tab1, height=10)
entry.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

# BUTTONS
button1 = Button(tab1, text="Reset", command=clear_text, width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab1, text="Summarize", command=get_summary, width=12, bg='#03A9F4', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3= Button(tab1, text="Get Abstractive Summary", command=get_abstractivesummary, width=20, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=1, padx=10, pady=10)


button3= Button(tab1, text="Speak", command=speak_summary, width=20, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=2, padx=10, pady=10)


button4 = Button(tab1, text="Clear Result", command=clear_display_result, width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=0, padx=10, pady=10)



# Display Screen For Result
tab1_display = Text(tab1)
tab1_display.grid(row=7, column=0, columnspan=5, padx=5, pady=5)

# FILE PROCESSING TAB
l1 = Label(tab2, text="Open File To Summarize")
l1.grid(row=1, column=1)

displayed_file = ScrolledText(tab2, height=7)  # Initial was Text(tab2)
displayed_file.grid(row=2, column=0, columnspan=5, padx=5, pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0 = Button(tab2, text="Open File", width=12, command=openfiles, bg='#c5cae9')
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="Reset ", width=12, command=clear_text_file, bg="#b9f6ca")
b1.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(tab2, text="Summarize", width=12, command=get_file_summary, bg='blue', fg='#fff')
b2.grid(row=3, column=2, padx=10, pady=10)


button3= Button(tab2, text="Speak", command=speak_filesummary, width=20, bg='#03A9F4', fg='#fff')
button3.grid(row=4, column=1, padx=10, pady=10)

b2 = Button(tab2, text="Abstractive Summarize", width=18, command=get_file_abstractivesummary, bg='blue', fg='#fff')
b2.grid(row=5, column=0, padx=10, pady=10)

b3 = Button(tab2, text="Clear Result", width=12, command=clear_text_result)
b3.grid(row=5, column=1, padx=10, pady=10)

b4 = Button(tab2, text="Close", width=12, command=window.destroy)
b4.grid(row=5, column=2, padx=10, pady=10)

# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, height=10)
tab2_display_text.grid(row=7, column=0, columnspan=8, padx=5, pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

# URL TAB
l1 = Label(tab3, text="Enter URL To Summarize")
l1.grid(row=1, column=0)

raw_entry = StringVar()
url_entry = Entry(tab3, textvariable=raw_entry, width=50)
url_entry.grid(row=1, column=1)

# BUTTONS


button3= Button(tab3, text="Speak", command=speak_comparesummary, width=20, bg='#03A9F4', fg='#fff')
button3.grid(row=3, column=1, padx=10, pady=10)

button1 = Button(tab3, text="Reset", command=clear_url_entry, width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab3, text="Get Text", command=get_text, width=12, bg='#03A9F4', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab3, text="Clear Result", command=clear_url_display, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab3, text="Abstractive Summarize", command=get_url_abstractivesummary, width=18, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

button4 = Button(tab3, text="Summarize", command=get_url_summary, width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=2, padx=10, pady=10)

# Display Screen For Result/6
url_display = ScrolledText(tab3, height=10)
url_display.grid(row=7, column=0, columnspan=8, padx=5, pady=5)

tab3_display_text = ScrolledText(tab3, height=10)
tab3_display_text.grid(row=10, column=0, columnspan=8, padx=5, pady=5)

# COMPARER TAB
l1 = Label(tab4, text="Enter Text To Summarize")
l1.grid(row=1, column=0)

entry1 = ScrolledText(tab4, height=10)
entry1.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

# BUTTONS
button1 = Button(tab4, text="Reset", command=clear_compare_text, width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab4, text="SpaCy", command=use_spacy, width=12, bg='red', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab4, text="Clear Result", command=clear_compare_display_result, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button6 = Button(tab4, text="NLTK", command=use_nltk, width=12, bg='#03A9F4', fg='#fff')
button6.grid(row=5, column=2, padx=10, pady=10)

button7 = Button(tab4, text="Abstractive Summary", command=use_abstractive, width=18, bg='#03A9F4', fg='#fff')
button7.grid(row=6, column=1, padx=10, pady=10)


# Display Screen For Result
tab4_display = ScrolledText(tab4, height=15)
tab4_display.grid(row=8, column=0, columnspan=8, padx=5, pady=5)

window.mainloop()