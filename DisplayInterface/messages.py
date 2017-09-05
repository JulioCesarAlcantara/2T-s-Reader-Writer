import tkinter
import tkinter.messagebox as tkMessageBox

def messageError(message):
   tkMessageBox.showwarning("Erro", message)

def messageWarning(message):
   tkMessageBox.showwarning("Warning", message)

def messageSucess(message):
   tkMessageBox.showwarning("Sucess", message)

