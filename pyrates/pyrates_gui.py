from tkinter import Tk, Canvas, Frame, Button
from typing import Sequence, Mapping

from pyrates.pyrates import PyRates
from pyrates.util.constants import Constants, Types


class PyRatesGUI:
    def __init__(self, master: Tk) -> None:
        self.__master: Tk = master
        self.__pyrates: PyRates = PyRates()
        self.__canvas: Canvas = Canvas(self.__master, bg=Constants.guiBackgroundColor, height=Constants.guiHeight, width=Constants.guiWidth)
        self.__canvas.pack()

        self.RenderAll()

    def RenderAll(self):
        self.Menu()
        self.RatesTableFrame()
        self.ConversionFrame()

    def Menu(self) -> None:
        menuFrame: Frame = Frame(self.__master, bg=Constants.guiBackgroundColor)
        menuFrame.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.1)

        homeButton = Button(menuFrame, text="Default View", bg='#070707', fg='#196619', command=self.RatesTable)
        homeButton.pack(side='left')

        exitButton = Button(menuFrame, text="Quit PyRates", bg='#070707', fg='#196619', command=self.__Exit)
        exitButton.pack(side='right')

    def RatesTable(self) -> None:
        pass

    def ConversionFrame(self):
        pass

    def __Exit(self) -> None:
        pass
    
    @staticmethod
    def Run() -> None:
        root: Tk = Tk()
        root.title(Constants.guiTitle)
        if not Constants.guiResizeable:
            root.resizable(False, False)
        PyRatesGUI(root)
        root.mainloop()


if __name__ == "__main__":
    PyRatesGUI.Run()
