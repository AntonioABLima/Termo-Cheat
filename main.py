import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from PIL import Image, ImageTk 

class TermoCheatApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Termo Cheat')
        self.master.geometry('720x800')
        self.master.resizable(False, False)
        self.master.configure(bg='#6e5c62')
        
        self.rows = 6
        self.columns = 5
        self.entry_grid = []
        
        self.custom_font = tkfont.Font(family="Arial", size=48, weight="normal")
        self.table = ttk.Frame(self.master, width=420, height=505)

        self.text_var00 = tk.StringVar()

        self.text_var =  []
        for i in range(35):
            self.text_var.append(tk.StringVar())

        self.index = 0
        for i in range(self.rows):
            row_entries = []
            row = ttk.Frame(self.table, width=420, height=80)
            for j in range(self.columns):
                entry = tk.Entry(
                    row, 
                    width=2, 
                    justify='center',
                    font=self.custom_font, 
                    bd=1,
                    fg='white',
                    textvariable=self.text_var[self.index],
                    validate="key",
                    validatecommand=(self.master.register(self.validate), "%P"),
                    insertbackground='#6e5c62',
                    bg='#6e5c62')
                
                match (self.index):
                    case 0: self.text_var[self.index].trace_add("write", self.convert_to_uppercase0)
                    case 1: self.text_var[self.index].trace_add("write", self.convert_to_uppercase1)
                    case 2: self.text_var[self.index].trace_add("write", self.convert_to_uppercase2)
                    case 3: self.text_var[self.index].trace_add("write", self.convert_to_uppercase3)
                    case 4: self.text_var[self.index].trace_add("write", self.convert_to_uppercase4)
                    case 5: self.text_var[self.index].trace_add("write", self.convert_to_uppercase5)
                    case 6: self.text_var[self.index].trace_add("write", self.convert_to_uppercase6)
                    case 7: self.text_var[self.index].trace_add("write", self.convert_to_uppercase7)
                    case 8: self.text_var[self.index].trace_add("write", self.convert_to_uppercase8)
                    case 9: self.text_var[self.index].trace_add("write", self.convert_to_uppercase9)
                    case 10: self.text_var[self.index].trace_add("write", self.convert_to_uppercase10)
                    case 11: self.text_var[self.index].trace_add("write", self.convert_to_uppercase11)
                    case 12: self.text_var[self.index].trace_add("write", self.convert_to_uppercase12)
                    case 13: self.text_var[self.index].trace_add("write", self.convert_to_uppercase13)
                    case 14: self.text_var[self.index].trace_add("write", self.convert_to_uppercase14)
                    case 15: self.text_var[self.index].trace_add("write", self.convert_to_uppercase15)
                    case 16: self.text_var[self.index].trace_add("write", self.convert_to_uppercase16)
                    case 17: self.text_var[self.index].trace_add("write", self.convert_to_uppercase17)
                    case 18: self.text_var[self.index].trace_add("write", self.convert_to_uppercase18)
                    case 19: self.text_var[self.index].trace_add("write", self.convert_to_uppercase19)
                    case 20: self.text_var[self.index].trace_add("write", self.convert_to_uppercase20)
                    case 21: self.text_var[self.index].trace_add("write", self.convert_to_uppercase21)
                    case 22: self.text_var[self.index].trace_add("write", self.convert_to_uppercase22)
                    case 23: self.text_var[self.index].trace_add("write", self.convert_to_uppercase23)
                    case 24: self.text_var[self.index].trace_add("write", self.convert_to_uppercase24)
                    case 25: self.text_var[self.index].trace_add("write", self.convert_to_uppercase25)
                    case 26: self.text_var[self.index].trace_add("write", self.convert_to_uppercase26)
                    case 27: self.text_var[self.index].trace_add("write", self.convert_to_uppercase27)
                    case 28: self.text_var[self.index].trace_add("write", self.convert_to_uppercase28)
                    case 29: self.text_var[self.index].trace_add("write", self.convert_to_uppercase29)
                    case 30: self.text_var[self.index].trace_add("write", self.convert_to_uppercase30)
      
                self.index += 1
                entry.grid(row=i, column=j)
                row_entries.append(entry)

            self.entry_grid.append(row_entries)
            row.pack()

        
        self.table.pack(expand=True)
        
    
    def validate(self, new_text):
        if len(new_text) == 0:
            return True
        if new_text.isalpha() and len(new_text) == 1:
            return True
        return False
    
    def convert_to_uppercase0(self, *args):
        self.text_var[0].set(self.text_var[0].get().upper())
    def convert_to_uppercase1(self, *args):
        self.text_var[1].set(self.text_var[1].get().upper())
    def convert_to_uppercase2(self, *args):
        self.text_var[2].set(self.text_var[2].get().upper())
    def convert_to_uppercase3(self, *args):
        self.text_var[3].set(self.text_var[3].get().upper())
    def convert_to_uppercase4(self, *args):
        self.text_var[4].set(self.text_var[4].get().upper())
    def convert_to_uppercase5(self, *args):
        self.text_var[5].set(self.text_var[5].get().upper())
    def convert_to_uppercase6(self, *args):
        self.text_var[6].set(self.text_var[6].get().upper())
    def convert_to_uppercase7(self, *args):
        self.text_var[7].set(self.text_var[6].get().upper())
    def convert_to_uppercase8(self, *args):
        self.text_var[8].set(self.text_var[6].get().upper())
    def convert_to_uppercase9(self, *args):
        self.text_var[9].set(self.text_var[6].get().upper())
    def convert_to_uppercase10(self, *args):
        self.text_var[10].set(self.text_var[6].get().upper())
    def convert_to_uppercase11(self, *args):
        self.text_var[11].set(self.text_var[6].get().upper())
    def convert_to_uppercase12(self, *args):
        self.text_var[12].set(self.text_var[6].get().upper())
    def convert_to_uppercase13(self, *args):
        self.text_var[13].set(self.text_var[6].get().upper())
    def convert_to_uppercase14(self, *args):
        self.text_var[14].set(self.text_var[6].get().upper())
    def convert_to_uppercase15(self, *args):
        self.text_var[15].set(self.text_var[6].get().upper())
    def convert_to_uppercase16(self, *args):
        self.text_var[16].set(self.text_var[6].get().upper())
    def convert_to_uppercase17(self, *args):
        self.text_var[17].set(self.text_var[17].get().upper())
    def convert_to_uppercase18(self, *args):
        self.text_var[18].set(self.text_var[18].get().upper())
    def convert_to_uppercase19(self, *args):
        self.text_var[19].set(self.text_var[19].get().upper())
    def convert_to_uppercase20(self, *args):
        self.text_var[20].set(self.text_var[20].get().upper())
    def convert_to_uppercase21(self, *args):
        self.text_var[21].set(self.text_var[21].get().upper())
    def convert_to_uppercase22(self, *args):
        self.text_var[22].set(self.text_var[22].get().upper())
    def convert_to_uppercase23(self, *args):
        self.text_var[23].set(self.text_var[23].get().upper())
    def convert_to_uppercase24(self, *args):
        self.text_var[24].set(self.text_var[24].get().upper())
    def convert_to_uppercase25(self, *args):
        self.text_var[25].set(self.text_var[25].get().upper())
    def convert_to_uppercase26(self, *args):
        self.text_var[26].set(self.text_var[26].get().upper())
    def convert_to_uppercase27(self, *args):
        self.text_var[27].set(self.text_var[27].get().upper())
    def convert_to_uppercase28(self, *args):
        self.text_var[28].set(self.text_var[28].get().upper())
    def convert_to_uppercase29(self, *args):
        self.text_var[29].set(self.text_var[29].get().upper())
    def convert_to_uppercase30(self, *args):
        self.text_var[30].set(self.text_var[30].get().upper())
    
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TermoCheatApp(root)
    
    for row in app.entry_grid:
        for entry in row:
            entry.config(validatecommand=(root.register(app.validate), "%P"))

    root.mainloop()
