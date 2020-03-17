from tkinter import Tk, Canvas, Frame, Button, Text, INSERT, DISABLED
from webbrowser import open_new
from typing import Sequence, Mapping

from pyrates.pyrates import PyRates
from pyrates.util.constants import GUI, Types


class PyRatesGUI:
    def __init__(self, master: Tk) -> None:
        self.__master: Tk = master
        self.__pyrates: PyRates = PyRates()
        self.__canvas: Canvas = Canvas(self.__master, bg=GUI.backgroundColor, height=GUI.height, width=GUI.width)
        self.__canvas.pack()

        self.__GUIMain()

    def __GUIMain(self) -> None:
        # Menu Frame
        menuFrame: Frame = Frame(master=self.__master, bg="#070605")
        menuFrame.place(relwidth=1, relheight=0.1)

        homeButton: Button = Button(
            master=menuFrame, 
            text="View Rates Table", 
            bg='#070707', 
            fg='#196619', 
            command=self.__UpdateRates
        )
        homeButton.pack(side='left')

        supportedCurrenciesButton: Button = Button(
            master=menuFrame, 
            text="View Supported Currencies", 
            bg='#070707', 
            fg='#196619', 
            command=self.__SupportedCurrencies
        )
        supportedCurrenciesButton.pack(side='left')

        sourceCodeButton: Button = Button(
            master=menuFrame, 
            text="Source Code", 
            bg='#070707', 
            fg='#196619', 
            command=self.__About
        )
        sourceCodeButton.pack(side='left')

        exitButton: Button = Button(
            master=menuFrame, 
            text="Quit PyRates", 
            bg='#070707', 
            fg='#196619', 
            command=self.__Exit)
        exitButton.pack(side='right')

        # Rates Frame
        ratesTableFrame: Frame = Frame(master=self.__master)
        ratesTableFrame.place(x=10, y=(GUI.height/4))

        ratesTableContent: Text = Text(
            master=ratesTableFrame,
            bg=GUI.backgroundColor, 
            fg="#196619", 
            height=100
        )
        ratesTableContent.insert(INSERT, self.__pyrates.__repr__())
        ratesTableContent.config(state=DISABLED)
        ratesTableContent.pack()
    

        # # Conversion Frame
        # conversionFrame: Frame = Frame(self.__master, bg="#077665")
        # conversionFrame.place(relwidth=0.5, relheight=0.9, y=(GUI.height/10))


    
    def __UpdateRates(self) -> None:
        pass

    def __SupportedCurrencies(self) -> None:
        pass

    def __About(self) -> None:
        open_new(GUI.source)

    def __Exit(self) -> None:
        pass
    
    @staticmethod
    def Run() -> None:
        root: Tk = Tk()
        root.title(GUI.title)
        if not GUI.resizeable:
            root.resizable(False, False)
        PyRatesGUI(root)
        root.mainloop()
