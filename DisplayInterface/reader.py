from doctest import master
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox

from DisplayInterface import Things

button_default_config = {
    "font": "Arial 15 normal",
    "bg": "gray",
    "fg": "white"
}


class Reader(Frame, object):
    """ Janela principal """

    def __init__(self, token=None):
        """ Método construtor da janela"""
        super().__init__(master=None)  # Aqui iniciamos a nossa superclasse (Frame)

        # Definições de titulos, largura
        # e altura da janela principal
        self.tree = None
        self.master.geometry ("600x500")
        self.master.title ("Reader")

        titulo=Label (master, text="Reader", font="Arial 60 normal")
        titulo.grid(column= 2, row=1)

        locationLabel = Label (master, text="Location", font="Arial 15 normal")
        locationLabel.grid (column=1, row=2)

        # self.parent = parent
        self.token = token
        self.combo(token)
        self.botaoReader()
        self.botaoBack()
        self.botaoSave()

        # Epacotamos o frame na janela
        # self.grid()

    def labelAtiv(self):
        titulo = Label (master, text="Waiting for Reading ...", font="Arial 10 normal")
        titulo.grid (column=2, row=4)

    def labelError(self):
        titulo = Label (master, text="Select a combo item...", font="Arial 10 normal")
        titulo.grid (column=2, row=4)

    def botaoReader(self):
        self.reader = Button(master, text="Reader", **button_default_config)
        self.reader["command"] = self.verificaLocalizacao
        self.reader.grid(column= 3, row=2)

    def botaoSave(self):
        self.reader = Button(self.parent, text="Save", **button_default_config)
        # self.reader["command"] = self.verificaLocalizacao
        self.reader.grid(column= 3, row=10)

    def botaoBack(self):
        self.reader = Button(self.parent, text="<< Back", **button_default_config)
        # self.reader["command"] = self.verificaLocalizacao
        self.reader.grid(column= 1, row=10)

    def combo(self,token):
        self.box_value = StringVar ()
        self.locationBox = Combobox (self.master, textvariable=self.box_value)
        self.locationBox.bind ("<<ComboboxSelected>>")

        a = Things
        b = a.searchLocations(token)
        locations = [('Choose a location...')]
        for c in b:
            locations.append(c.loca_room)

        self.locationBox['values'] = locations
        self.locationBox.current (0)
        self.locationBox.grid(column=2, row=2)

    def verificaLocalizacao(self):

        if self.locationBox.get() == "Choose a location":
            self.labelError()
        else:

            self.labelAtiv()
            self._setup_widgets ()
            self._build_tree ()

    def _setup_widgets(self):

        msg = ttk.Label(wraplength="4i",
            padding=(0, 5, 0, 0))
        msg.grid(column=5)
        container = ttk.Frame()
        container.grid(column=2, row=6)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=car_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        # hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        # hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in car_header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 1))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))
        for item in car_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)+50
                if self.tree.column(car_header[ix],width=None)<col_w:
                    self.tree.column(car_header[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))

car_header = ['Code', 'Location']


car_list = [
    ('1234', 'Lab.3'),
    ('2342', 'Lab.3'),
    ('5321', 'Lab.3'),
    ('4642', 'Lab.3'),
    ('2345', 'Lab.3'),
    ('0987', 'Lab.3'),
    ('7890', 'Lab.3'),
    ('5678', 'Lab.3'),
    ('4325', 'Lab.3'),
    ('7896', 'Lab.3'),
    ('9487', 'Lab.3'),
    ('0987', 'Lab.3'),
    ('0983', 'Lab.3'),
    ('7365', 'Lab.3'),
    ('0293', 'Lab.3')]

if __name__ == '__main__':
    root = tk.Tk()
    window = Reader()
    window.mainloop()

    # root = tk.Tk()
    #
    # mc_listbox = Window()
    # root.mainloop()