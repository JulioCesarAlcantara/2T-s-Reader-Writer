from tkinter import *
import tkinter.messagebox as tkMsgBox
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter.ttk import Combobox

from DisplayInterface import Things, messages

button_default_config = {
    "font": "Arial 10 normal",
    "bg": "gray",
    "fg": "white"
}

class ListThings(Frame):

    value_of_combo = 'X'


    def __init__(self, parent=None, token=None):

        super ().__init__ (master=None)
        self.token = token
        self.parent = parent
        self.label()
        self.comboLocation()
        self.comboStatus()
        # self.botaoSearch1()
        self.botaoSearch2()
        self.botaoBack()

        print(token)


        # self.token = self.token
        self.a = Things
        self.b = self.a.searchLocations (token)
        self.car_list = []
        self.car_header = ['Code', 'Name', 'Location', 'Status']

        self._setup_widgets ()
        self._build_tree ()


    def botaoSearch1(self):
        self.search1 = Button(self.parent, text="Search", **button_default_config)
        self.search1["command"]=self.chamaTabelaLocation
        self.search1.grid(column=2, row=1)

    def botaoSearch2(self):
        self.search2 = Button(self.parent, text="Search", **button_default_config)
        self.search2["command"]=self.chamaTabela
        self.search2.grid(column=2, row=2)

    def botaoBack(self):
        self.back = Button(self.parent, text="<< Back", **button_default_config)
        self.back.grid(column=0, row=7)
    def label(self):
        self.msg = Label(self.parent, text="List Things", font="Arial 20 normal")
        self.msg.grid(column=1, row=0)

    def comboLocation(self):
        # print(self.token)
        a = Things
        b = a.searchLocations(self.token)
        location= b

        locations = [('Choose a location...')]
        for c in location:
            locations.append (c.loca_room)

        self.box_value = StringVar ()
        self.locationBox = Combobox (self.master, textvariable=self.box_value)
        self.locationBox.bind ("<<ComboboxSelected>>")

        self.locationBox['values'] = locations
        self.locationBox.current (0)
        self.locationBox.grid(column=1, row=1)

    def comboStatus(self):
        self.box_value2 = StringVar()
        self.box2 = ttk.Combobox(self.parent, textvariable=self.box_value2)
        self.box2['values'] = ('Select a Status...', 'Active', 'Inactive')
        self.box2.current(0)
        self.box2.grid(column=1, row=2)

    def chamaTabela(self):
        # self.zeraTabela()
        things = Things
        mens = messages
        if self.locationBox.get() == "Choose a location..." and self.box2.get() == "Select a Status...":
            mens.messageError ("Please select a Location or Status for consultation. Or, if you prefer, select both.")
        elif self.locationBox.get() == "Choose a location..." and self.box2.get() == "Active":
            dados = things.searchThingsActived(self.token)
            #monta tabela com somente coisas ativas;
        elif self.locationBox.get() == "Choose a location..." and self.box2.get() == "Inactive":
            dados = things.searchThingsInactives (self.token)

        elif self.locationBox.get() != "Choose a location..." and self.box2.get() == "Select a Status...":
            selected = [a for a in self.b if a.loca_room == self.locationBox.get ()]
            dados = things.searchThingsByLocation (self.token, str (selected[0].loca_id))

        elif self.locationBox.get() != "Choose a location..." and self.box2.get() == "Active":
            selected = [a for a in self.b if a.loca_room == self.locationBox.get ()]
            dados = things.searchThingsActivesByLocation (self.token ,str (selected[0].loca_id))

        else:
            selected = [a for a in self.b if a.loca_room == self.locationBox.get ()]
            dados = things.searchThingsInactivesByLocation (self.token, str (selected[0].loca_id))

        for b in dados:
            # print(b.code_things, b.description, b.location, b.state)
            self.car_list.append ([b.code_things, b.description, b.location['loca_room'], b.tag_activated])


        self._setup_widgets ()
        self._build_tree ()

    def chamaTabelaLocation(self):
        mens = messages
        if self.locationBox.get()=="Select a Location...":
            mens.messageError("ERROR", "Select a valid option!")
        elif self.locationBox.get() != "Select a Location..." and self.box2.get()=="Inactive":
            mens.messageError("ERROR", "Select a valid option!")
        else:
            selected = [a for a in self.b if a.loca_room == self.locationBox.get ()]

            things = Things
            dados = things.searchThingsByLocation (self.token, str (selected[0].loca_id))


            for b in dados:
                # print(b.code_things, b.description, b.location, b.state)
                self.car_list.append ([b.code_things, b.description, b.location['loca_room'], b.tag_activated])

        self._setup_widgets ()
        self._build_tree ()

    def zeraTabela(self):
        self.__init__()

    def _setup_widgets(self):

        msg = ttk.Label(wraplength="4i",
                        padding=(0, 5, 0, 0))
        msg.grid(column=5)
        container = ttk.Frame()
        container.grid(column=1, row=6)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=self.car_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        # hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        # hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in self.car_header:
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
                if self.tree.column(self.car_header[ix], width=None) < col_w:
                    self.tree.column(self.car_header[ix], width=col_w)


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


car_list = []

# car_list = [
#     ('1234','Computer', 'Lab.3', 'Active'),
#     ('2342', 'Table', 'Lab.3', 'Active'),
#     ('5321', 'Chair', 'Lab.3', 'Active'),
#     ('4642', 'Screen', 'Lab.3', 'Active')]

if __name__ == '__main__':
    root = Tk()
    app = ListThings(root)
    root.mainloop()