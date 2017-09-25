from tkinter import *
from DisplayInterface.reader import Reader
from DisplayInterface.Writer import Writer
from DisplayInterface.listThings import ListThings
from UserManager.login import Login

# Guarda as configurações padrão para os
# botões que serão definidos mais tarde
button_default_config = {
    "font": "Arial 10 normal",
    "bg": "gray",
    "fg": "white"
}


class Window():
    """ Janela principal """

    def __init__(self, token =NONE, name=NONE):
        """ Método construtor da janela"""
        super().__init__(master=None)  # Aqui iniciamos a nossa superclasse (Frame)

        # Definições de titulos, largura
        # e altura da janela principal
        self.master.geometry("500x200")
        self.master.title("Welcome")
        self.token = token
        #########################################

        msg = Label(self, text="Raspberry PI Reader Prototype")
        msg2 = Label(self, text="Welcome, "+ name+ ". This prototype will\n help you in controlling patrimony.")
        msgmenu = Label(self, text="Menu")
        msg.grid(row=0, column=1, sticky=NSEW)
        msg2.grid(row=5, column=1, sticky=NSEW)
        msgmenu.grid(row=2, column=0, sticky=NSEW)
        #########################################

        self.buttonReader()
        self.buttonWriter()
        self.callListThings()
        self.buttonSynchronize()
        self.buttonQuit()

        # Ao criar outro botão devemos fazer da mesma forma
        # para que fique tudo igual, passaremos o mesmo
        # dicionário de attributos que passamos ao primeiro
        # button2 = Button(self, text="Writer", **button_default_config)
        #
        # # Definimos outra fonte ao 2° botão, pois
        # # as celulas irão se ajustar automaticamente
        # #button2.configure(font="Arial 20 normal")
        #
        # # Configurando novamente o grid
        # button2.grid(row=4, column=0, sticky=NSEW)
        #
        # ###############################################
        # button3 = Button (self, text="List Things", **button_default_config)
        # button3.grid(row=5, column=0, sticky=NSEW)
        # button4 = Button(self, text="Synchronization", **button_default_config)
        # button4.grid(row=6, column=0, sticky=NSEW)
        # button5 = Button(self, text="Quit", **button_default_config, command=self.quit)
        # button5.grid(row=7, column=0, sticky=NSEW)
        ###############################################

        # Essa é a parte mais importante, pois, define o
        # esticamento de cada celula do grid. Se possivel
        # comente as 2 linhas abaixo e teste para entender melhor
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=7)

        # Epacotamos o frame na janela
        self.pack(fill=BOTH, expand=True)

    def buttonReader(self):
        self.button1 = Button (self, text="Reader", command= lambda : self.callReader(self.token), **button_default_config)
        self.button1.grid (row=3, column=0, sticky=NSEW)

    def buttonWriter(self):
        self.button2 = Button (self, text="Writer", command= lambda : self.callWriter(self.token), **button_default_config)
        self.button2.grid (row=4, column=0, sticky=NSEW)

    def buttonListThing(self):
        self.button3 = Button (self, text="List Things", command= lambda : self.callListThings(self.token), **button_default_config)
        self.button3.grid (row=5, column=0, sticky=NSEW)

    def buttonSynchronize(self):
        self.button4 = Button (self, text="Synchronization", command= lambda : self.callSynchronize(self.token), **button_default_config)
        self.button4.grid (row=6, column=0, sticky=NSEW)

    def buttonQuit(self):
        self.button5 = Button (self, text="Quit", command= lambda : self.callQuit(), **button_default_config)
        self.button5.grid (row=7, column=0, sticky=NSEW)

    def callReader(self, token=None):
        global window
        self.destroy ()
        reader = Reader ()
        window.mainloop ()

    def callWriter(self, token=None):
        global window
        self.destroy ()
        writer = Writer ()
        writer.mainloop ()

    def callListThings(self, token=None):
        global window
        self.destroy ()
        listThings = ListThings ()
        listThings.mainloop ()

    def callSynchronize(self, token=None):
        global window
        self.destroy ()
        # reader = Reader (self.token)
        # window.mainloop ()

    def callQuit(self, token=None):
        global window
        self.destroy ()
        login = Login ()
        window.mainloop ()

if __name__ == '__main__':
    window = Window()
    window.mainloop()
