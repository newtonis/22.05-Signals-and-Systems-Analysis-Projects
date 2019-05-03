import tkinter as tk
from Globals import config


class StartMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=40,
            text="Seleccionar modo",
            font=config.LARGE_FONT,
            background="#ccffd5"
        )

        buttonFrame = tk.Frame(self)

        self.button1 = tk.Button(
            buttonFrame,
            height=5,
            width=20,
            text="EFECTO PREDEFINIDO",
            font=config.SMALL_FONT,
            background="#b8caff",
            command=self.predefinido
        )

        self.button2 = tk.Button(
            buttonFrame,
            height=5,
            width=20,
            text="EFECTO PERSONALIZADO",
            font=config.SMALL_FONT,
            background="#fff49f",
            command=self.goToPersonalizado
        )

        self.title.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        f = tk.Frame(self)
        f.configure(height=200)
        f.pack(side=tk.TOP, expand=1, fill = tk.X)

        self.button1.pack(side=tk.LEFT, expand=1, fill=tk.X)
        self.button2.pack(side=tk.RIGHT, expand=1, fill=tk.X)
        buttonFrame.pack(side=tk.TOP, expand=1, fill=tk.X)

        f = tk.Frame(self)
        f.configure(height=100)
        f.pack(side=tk.TOP, expand=1, fill = tk.X)

    def predefinido(self):
        pass

    def goToPersonalizado(self):
        from Menus.PersonalizadoMenu import PersonalizadoMenu
        self.controller.showFrame(PersonalizadoMenu)

    def focus(self):
        pass
