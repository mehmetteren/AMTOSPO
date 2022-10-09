import tkinter as tk
from tkinter import messagebox as ms


class GUI:
    choice = ""
    link = ""

    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, height=400, width=700)
        self.canvas.pack()

        self.frame_left = tk.Frame(self.window, bg='grey')
        self.frame_left.place(relx=0, rely=0, relheight=1, relwidth=0.12)

        self.frame_rightUp = tk.Frame(self.window, bg='light grey')
        self.frame_rightUp.place(relx=0.13, rely=0, relheight=0.5, relwidth=0.87)

        self.frame_rightDown = tk.Frame(self.window, bg='light grey')
        self.frame_rightDown.place(relx=0.13, rely=0.52, relheight=0.48, relwidth=0.87)

        tk.Label(self.frame_rightUp, bg='light grey', text='Welcome to amtospo!', font="Verdana 25 bold").pack(anchor='s',
                                                                                                          padx=25,
                                                                                                          pady=25)

        tk.Label(self.frame_rightUp, bg='light grey', text='Playlist from: ', font="Verdana 17 bold").pack(anchor='sw',
                                                                                                      padx=10,
                                                                                                      pady=10)

        self.transType_default = tk.StringVar(self.frame_rightUp)
        self.transType_default.set("\t")

        self.transType_menu = tk.OptionMenu(self.frame_rightUp, self.transType_default, 'Youtube Music', 'Apple Music')
        self.transType_menu.pack(padx=10, pady=10, anchor='sw')

        tk.Label(self.frame_rightDown, bg='light grey', text='File name or Url: ', font="Verdana 17 bold").pack(anchor='nw',
                                                                                                           padx=10,
                                                                                                           pady=10)

        self.text_space = tk.Text(self.frame_rightDown, bg='light blue', height=0.5, width=50)
        self.text_space.tag_configure('style', foreground='#bfbfbf', font=('Verdana', 7, 'bold'))
        self.text_space.pack(anchor='nw', padx=10, pady=10)

        self.text = 'Paste link or enter XML file name...'
        self.text_space.insert('end', self.text, 'style')

        self.send_button = tk.Button(self.frame_rightDown, text='Send', command=self.send)
        self.send_button.pack(anchor='sw', padx=10, pady=10)

    #

    def sendText(self):
        if self.transType_default and self.text != 'Paste link or enter XML file name..':
            return self.text
        else:
            message = 'Please enter informations correctly!'

        ms.showwarning('Error', message)

    def sendChoice(self):
        if self.transType_default and self.text != 'Paste link or enter XML file name..':
            return self.transType_default
        else:
            message = 'Please enter informations correctly!'

        ms.showwarning('Error', message)

    def send(self):
        self.choice = self.transType_default.get()
        self.link = self.text_space.get("1.0", "end")
