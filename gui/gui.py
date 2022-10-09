import tkinter as tk
from tkinter import messagebox as ms


class GUI:

    window = tk.Tk()
    canvas = tk.Canvas(window, height=400, width=700)
    canvas.pack()

    frame_left = tk.Frame(window, bg='grey')
    frame_left.place(relx=0, rely=0, relheight=1, relwidth=0.12)

    frame_rightUp = tk.Frame(window, bg='light grey')
    frame_rightUp.place(relx=0.13, rely=0, relheight=0.5, relwidth=0.87)

    frame_rightDown = tk.Frame(window, bg='light grey')
    frame_rightDown.place(relx=0.13, rely=0.52, relheight=0.48, relwidth=0.87)

    tk.Label(frame_rightUp, bg='light grey', text='Welcome to amtospo!', font="Verdana 25 bold").pack(anchor='s',
                                                                                                      padx=25,
                                                                                                      pady=25)

    tk.Label(frame_rightUp, bg='light grey', text='Playlist from: ', font="Verdana 17 bold").pack(anchor='sw', padx=10,
                                                                                                  pady=10)

    transType_default = tk.StringVar(frame_rightUp)
    transType_default.set("\t")

    transType_menu = tk.OptionMenu(frame_rightUp, transType_default, 'Youtube Music', 'Apple Music')
    transType_menu.pack(padx=10, pady=10, anchor='sw')

    tk.Label(frame_rightDown, bg='light grey', text='File name or Url: ', font="Verdana 17 bold").pack(anchor='nw',
                                                                                                       padx=10,
                                                                                                       pady=10)

    text_space = tk.Text(frame_rightDown, bg='light blue', height=0.5, width=50)
    text_space.tag_configure('style', foreground='#bfbfbf', font=('Verdana', 7, 'bold'))
    text_space.pack(anchor='nw', padx=10, pady=10)

    text = 'Paste link or enter XML file name...'
    text_space.insert('end', text, 'style')

    #
    def send(self):
        if self.transType_default and self.text != 'Paste link or enter XML file name..':
            return self.transType_default
        else:
            message = 'Please enter informations correctly!'

        ms.showwarning('Error', message)

    send_button = tk.Button(frame_rightDown, text='Send', command=send)
    send_button.pack(anchor='sw', padx=10, pady=10)

    def __init__(self):
        return





if send() == 'Youtube Music':
    final_song_name = axp.get_song_name()
    # final_song_name = axp.remove_feat_from_song(song_name)
    # artist_name = axp.get_artist_name()
    # album_name = axp.get_album_name()
    # final_album_name = axp.remove_feat_from_album(album_name)

window.mainloop()
