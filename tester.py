from tkinter import *
import requests
import time
import random
import schedule

root = Tk()
root.title("Word of the day")
root.geometry("500x500")

class Window():
    def __innit__(self, )