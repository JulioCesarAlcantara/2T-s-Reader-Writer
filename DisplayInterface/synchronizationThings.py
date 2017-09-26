import requests
from tkinter import *
import tkinter.messagebox as tkMsgBox
import tkinter.font as tkFont
import tkinter.ttk as ttk
from Model.ThingsModel import ThingsModel

button_default_config = {
    "font": "Arial 10 normal",
    "bg": "gray",
    "fg": "white"
}

class SynchronizationThings():
    def __init__(self, parent):
        self.parent = parent
        self.label()
        self.chamaTabela()
        self.botao()

    def botao(self):
        self.synchronization = Button(self.parent, text="Synchronization", **button_default_config)
        #self.synchronization["command"] = self.chamaTabela
        self.synchronization.grid(column=2, row=7)
        self.back = Button(self.parent, text="<< Back", **button_default_config)
        self.back.grid(column=0, row=7)

    def label(self):
        self.msg = Label(self.parent, text="Synchronization", font="Arial 20 normal")
        self.msg.grid(column=1, row=0)


    def chamaTabela(self):
            self._setup_widgets()
            self._build_tree()

    def msgError(self):
        tkMsgBox.showwarning("ERROR", "Select a valid option!")

    def _setup_widgets(self):

        msg = ttk.Label(wraplength="4i",
                        padding=(0, 5, 0, 0))
        msg.grid(column=5)
        container = ttk.Frame()
        container.grid(column=1, row=6)
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
                col_w = tkFont.Font().measure(val)
                if self.tree.column(car_header[ix], width=None) < col_w:
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


car_header = ['Code', 'Name', 'Location']
car_list = [
    ('1234', 'Computer', 'Lab.3'),
    ('2342', 'Table', 'Lab.3'),
    ('5321', 'Chair', 'Lab.3'),
    ('4642', 'Screen', 'Lab.3')]



def synchronizationThings(Token, Location, nThings):
        try:
            url = "https://dg-2ts-server.herokuapp.com/"
            response = requests.get(url + "synchronize_location/token="+ Token +"&locaid="+Location+"&num=" + nThings)
            data = response.json()

            if response.ok:
                try:
                    if data["response"] == None:
                        print("Aqui")
                    else :
                        print(data["response"])
                except Exception as e:
                    u = ThingsModel (**data)
                    print (u.token)

        except Exception as e:
            print ("Erro no Servidor")

synchronizationThings("asdfasdfasdfz","8", "039583")

if __name__ == '__main__':
    root = Tk()
    app = SynchronizationThings(root)
    root.mainloop()