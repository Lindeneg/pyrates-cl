import sys
from tkinter import Tk, Canvas, Frame, Button, Text, Scrollbar, INSERT, DISABLED, RIGHT, Y
from webbrowser import open_new
from typing import Sequence, Mapping

from pyrates.pyrates import PyRates
from pyrates.util.constants import GUI, Types, Constants


class PyRatesGUI:
    """
    PyRates GUI implementation using Tkinter

    To run the GUI, call the static method Run()
    """
    def __init__(self, master: Tk) -> None:
        self.__master: Tk = master
        self.__pyrates: PyRates = PyRates()
        self.__canvas: Canvas = Canvas(self.__master, bg=GUI.backgroundColor, height=GUI.height, width=GUI.width)
        self.__canvas.pack()
        self.__RenderAll()

    def __RenderAll(self) -> None:
        self.__ComponentMenuView()
        self.__ComponentRatesTableView()
        self.__ComponentConversionView()
    
    def __ComponentMenuView(self) -> None:
        menuFrame: Frame = Frame(master=self.__master, bg=GUI.backgroundColor)
        menuFrame.place(relwidth=0.98, relheight=0.1, x=GUI.xOffset, y=GUI.yOffset)

        viewRatesButton: Button = Button(
            master=menuFrame, 
            text="View Rates Table", 
            bg=GUI.buttonColor, 
            fg=GUI.textColor, 
            command=self.__CommandViewRates
        )
        viewRatesButton.pack(side='left')

        supportedCurrenciesButton: Button = Button(
            master=menuFrame, 
            text="View Supported Currencies", 
            bg=GUI.buttonColor, 
            fg=GUI.textColor, 
            command=self.__CommandViewSupportedCurrencies
        )
        supportedCurrenciesButton.pack(side='left')

        updateRatesButton: Button = Button(
            master=menuFrame, 
            text="Update Rates", 
            bg=GUI.buttonColor, 
            fg=GUI.textColor, 
            command=self.__CommandUpdateRates
        )
        updateRatesButton.pack(side='left')

        exitButton: Button = Button(
            master=menuFrame, 
            text="Quit PyRates", 
            bg=GUI.buttonColor,  
            fg=GUI.textColor, 
            command=self.__CommandExit)
        exitButton.pack(side='right')

        sourceCodeButton: Button = Button(
            master=menuFrame, 
            text="Source Code", 
            bg=GUI.buttonColor, 
            fg=GUI.textColor, 
            command=self.__CommandAbout
        )
        sourceCodeButton.pack(side='right')

    def __ComponentRatesTableView(self, viewSupportedCurrencies: bool = False) -> None:
        ratesTableFrame: Frame = Frame(master=self.__master)
        ratesTableFrame.place(x=GUI.xOffset, y=(GUI.height/3))

        ratesTableContent: Text = Text(
            master=ratesTableFrame,
            bg=GUI.backgroundColor, 
            fg=GUI.textColor,
            height=GUI.componentTableHeight
        )
        text: str
        if viewSupportedCurrencies:
            text = self.__StringifySupportedCurrencies()
        else:
            text = self.__pyrates.__repr__()
        ratesTableContent.insert(INSERT, text)
        ratesTableContent.config(state=DISABLED)
        ratesTableContent.pack()

    def __ComponentConversionView(self) -> None:
        conversionFrame: Frame = Frame(self.__master, bg="#FF0000", height=150, width=645)
        conversionFrame.place(x=GUI.xOffset, y=(GUI.height-(GUI.height * 0.9)))

    def __CommandUpdateRates(self) -> None:
        updateSuccessful: bool = self.__pyrates.UpdateRates()
        if not updateSuccessful:
            pass
        else:
            self.__ComponentRatesTableView()

    def __CommandViewRates(self) -> None:
        self.__ComponentRatesTableView()

    def __CommandViewSupportedCurrencies(self) -> None:
        self.__ComponentRatesTableView(viewSupportedCurrencies=True)

    def __CommandAbout(self) -> None:
        open_new(GUI.source)

    def __CommandExit(self) -> None:
        self.__master.destroy()
        sys.exit()

    def __StringifySupportedCurrencies(self) -> str:
        result: str = "CODE - NAME\n\n"
        for code, name in Constants.currencies.items():
            result += f"{code.upper()}  - {name.capitalize()}\n"
        return result

    @staticmethod
    def Run() -> None:
        root: Tk = Tk()
        root.title(GUI.title)
        if not GUI.resizeable:
            root.resizable(False, False)
        PyRatesGUI(root)
        root.mainloop()
