from Tkinter import *

import devices.Time
import numpy
from controller.Global import *
import locale


class Controller:
    locale.setlocale(locale.LC_ALL, 'en_GB.utf8')

    def close(self):
        self.root.destroy()

    def __init__(self):
        # ratio constants
        self.root = Tk()
        self.root.attributes('-fullscreen', True)
        self.root.focus_set()

        self.root.bind('<Escape>', self.close)
        self.root.config(cursor='none')

        win_width = self.root.winfo_screenwidth()  # 1280
        win_height = self.root.winfo_screenheight()  # 800

        self.objects = []
        self.canvas = Canvas(self.root, width=win_width, height=win_height, bg=Global.OFFBgColor)
        self.canvas.pack()
        self.timer = devices.Time.Time()

    def add_object(self, gui_object):
        gui_object.add_to_canvas(self.canvas)
        self.objects.append(gui_object)

    def _new_update_all(self):
        for gui_object in self.objects:
            gui_object.set_text(self.timer.time)
        self.canvas.after(10, self._new_update_all)

    def start(self):
        self.canvas.after(10, self._new_update_all())
        # main loop
        self.root.mainloop()
