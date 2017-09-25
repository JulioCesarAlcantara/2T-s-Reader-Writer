from tkinter import *
import tkinter.messagebox as tkMsgBox
import tkinter.font as tkFont
import tkinter.ttk as ttk

button_default_config = {
    "font": "Arial 10 normal",
    "bg": "gray",
    "fg": "white"
}

class ListThings:

    value_of_combo = 'X'


    def __init__(self, parent):
        self.parent = parent
        self.label()
        self.combo()
        self.botao()

    def botao(self):
        self.search1 = Button(self.parent, text="Search", **button_default_config)
        self.search1["command"]=self.chamaTabela
        self.search1.grid(column=2, row=1)
        self.search2 = Button(self.parent, text="Search", **button_default_config)
        self.search2["command"]=self.chamaTabela
        self.search2.grid(column=2, row=2)
        self.back = Button(self.parent, text="<< Back", **button_default_config)
        self.back.grid(column=0, row=7)
    def label(self):
        self.msg = Label(self.parent, text="List Things", font="Arial 20 normal")
        self.msg.grid(column=1, row=0)

    def combo(self):
        self.box_value1 = StringVar()
        self.box1 = ttk.Combobox(self.parent, textvariable=self.box_value1)
        self.box1['values'] = ('Select a Location...', 'Lab 2', 'Lab 3')
        self.box1.current(0)
        self.box1.grid(column=1, row=1)
        self.box_value2 = StringVar()
        self.box2 = ttk.Combobox(self.parent, textvariable=self.box_value2)
        self.box2['values'] = ('Select a Status...', 'Active', 'Inactive')
        self.box2.current(0)
        self.box2.grid(column=1, row=2)

    def chamaTabela(self):
        if self.box1.get()=="Select a Location...":
            self.msgError()
        elif self.box2.get()=="Select a Status...":
            self.msgError()
        else:
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
car_header = ['Code','Name', 'Location', 'Status']
car_list = [
    ('1234','Computer', 'Lab.3', 'Active'),
    ('2342', 'Table', 'Lab.3', 'Active'),
    ('5321', 'Chair', 'Lab.3', 'Active'),
    ('4642', 'Screen', 'Lab.3', 'Active')]

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()