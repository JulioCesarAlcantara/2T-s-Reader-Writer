from doctest import master
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox

from DisplayInterface import Things, messages

button_default_config = {
    "font": "Arial 15 normal",
    "bg": "gray",
    "fg": "white"
}


class Writer(Frame, object):
    """ Janela principal """

    def __init__(self, parent=None):
        """ Método construtor da janela"""
        super().__init__(master=None)  # Aqui iniciamos a nossa superclasse (Frame)

        self.token = 'asdfasdfasdfz'
        self.a = Things
        self.b = self.a.searchLocations ('asdfasdfasdfz')
        self.car_list = []
        # Definições de titulos, largura
        # e altura da janela principal
        self.tree = None
        self.master.geometry ("600x700")
        self.master.title ("Writer")

        titulo=Label (master, text="Writer", font="Arial 60 normal")
        titulo.grid(column= 2, row=1)

        labelCode = Label (master, text="Code", font="Arial 15 normal")
        labelCode.grid (column=1, row=2)

        locationLabel = Label (master, text="Location", font="Arial 15 normal")
        locationLabel.grid (column=1, row=3)

        self.parent = parent
        self.combo()
        self.botaoFilter1()
        self.botaoFilter2()
        self.botaoBack()
        self.botaoSave()
        self.textFieldCodeSearch()

    def labelError(self):
        titulo = Label (master, text="Select a combo item...", font="Arial 10 normal")
        titulo.grid (column=2, row=4)

    def botaoFilter1(self):
        self.reader = Button(master, text="Search", **button_default_config)
        self.reader["command"] = self.verificaLocalizacao
        self.reader.grid(column= 3, row=2)

    def botaoFilter2(self):
        self.reader = Button(master, text="Search", **button_default_config)
        self.reader["command"] = self.verificaLocalizacao
        self.reader.grid(column= 3, row=3)

    def botaoSave(self):
        self.reader = Button(self.parent, text="Active", **button_default_config)
        # self.reader["command"] = self.verificaLocalizacao
        self.reader.grid(column= 3, row=10)

    def botaoBack(self):
        self.reader = Button(self.parent, text="<< Back", **button_default_config)
        # self.reader["command"] = self.verificaLocalizacao
        self.reader.grid(column= 1, row=10)

    def combo(self, dados=None):
        a = Things
        b = a.searchLocations ('asdfasdfasdfz')

        locations = [('Choose a location...')]
        locationsId = []
        for c in b:
            locations.append (c.loca_room)
            # print("aqui :" + c.loca_id)

        self.box_value = StringVar ()
        # self.locationBox = ttk.Combobox (self.master, state="readonly", choices=locationsId, values=locations)
        self.locationBox = Combobox (self.master, textvariable=self.box_value)
        self.locationBox.bind ("<<ComboboxSelected>>")

        self.locationBox['values'] = locations
        self.locationBox.current (0)
        self.locationBox.grid(column=2, row=3)

    def textFieldCodeSearch(self):
        self.fontePadrao = ("Arial", "10")
        self.terceiroContainer = Frame (master)
        self.terceiroContainer["padx"] =10
        self.terceiroContainer.grid (column=2, row=2)

        self.code = Entry (self.terceiroContainer)
        self.code["width"] = 29
        self.code["font"] = self.fontePadrao
        self.code.grid ()

    def verificaLocalizacao(self):

        # print(self.locationBox.get())
        # selected = [a for a in self.b if a.loca_room == self.locationBox.get()]
        # print(selected[0].loca_id)
        #
        if self.locationBox.get() == "Choose a location...":
            mens = messages
            mens.messageError("Select a location !")
        else:
            selected = [a for a in self.b if a.loca_room == self.locationBox.get ()]
            things = Things
            dados = things.searchThingsByLocation (self.token, str(selected[0].loca_id))

            for b in dados:
                # print(b.code_things, b.description, b.location, b.state)
                self.car_list.append ([b.code_things, b.description, b.location['loca_room'], b.tag_activated])

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
        for item in self.car_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(car_header[ix],width=None)<col_w:
                    self.tree.column(car_header[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    # data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))

car_header = ['Code','Name','Location', 'Status']

# things = Things
# dados = things.searchThingsByLocation('asdfasdfasdfz', '7')
# car_list = []
# for b in dados:
#     # print(b.code_things, b.description, b.location, b.state)
#     car_list.append([b.code_things, b.description, b.location['loca_room'], b.state])



#comentário aqui

if __name__ == '__main__':
    root = tk.Tk()
    window = Writer()
    window.mainloop()

    # root = tk.Tk()
    #
    # mc_listbox = Window()
    # root.mainloop()