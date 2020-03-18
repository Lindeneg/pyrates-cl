import sys
from time import time
from datetime import datetime
from tkinter import (
    Tk, Canvas, Frame, Button, 
    Text, Scrollbar, Entry, Label, 
    INSERT, DISABLED, RIGHT, LEFT, Y
)
from webbrowser import open_new
from typing import Sequence, Mapping, Callable, Union

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

    def __RenderAll(self, mainView: str = "currentRates", utilityContent: str = "PyRatesGUI - 0.2\n\nMake a Conversion") -> None:
        self.__ComponentMenuView()
        if mainView == "currentRates":
            self.__ComponentRatesTableView()
        else:
            self.__ComponentRatesTableView(viewSupportedCurrencies=True)
        self.__ComponentConversionView()
        self.__ComponentUtilityView(content=utilityContent)
    
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
        viewRatesButton.pack(side=LEFT)

        supportedCurrenciesButton: Button = Button(
            master=menuFrame, 
            text="View Supported Currencies", 
            bg=GUI.buttonColor, 
            fg=GUI.textColor, 
            command=self.__CommandViewSupportedCurrencies
        )
        supportedCurrenciesButton.pack(side=LEFT)

        updateRatesButton: Button = Button(
            master=menuFrame, 
            text="Update Rates", 
            bg=GUI.buttonColor, 
            fg=GUI.textColor, 
            command=self.__CommandUpdateRates
        )
        updateRatesButton.pack(side=LEFT)

        exitButton: Button = Button(
            master=menuFrame, 
            text="Quit PyRates", 
            bg=GUI.buttonColor,  
            fg=GUI.textColor, 
            command=self.__CommandExit)
        exitButton.pack(side=RIGHT)

        sourceCodeButton: Button = Button(
            master=menuFrame, 
            text="Source Code", 
            bg=GUI.buttonColor, 
            fg=GUI.textColor, 
            command=self.__CommandAbout
        )
        sourceCodeButton.pack(side=RIGHT)

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
        conversionFrame: Frame = Frame(
            self.__master, 
            bg=GUI.backgroundColor, 
            height=GUI.conversionHeight, 
            width=GUI.conversionWidth
        )
        conversionFrame.place(x=GUI.xOffset, y=(GUI.height-(GUI.height * 0.9)))

        amoutInputLabel: Label = Label(
            conversionFrame, 
            text="Amount To Convert:    ", 
            bg=GUI.backgroundColor, 
            fg=GUI.textColor
        ).grid(row=0)
        amountInputEntry: Entry = Entry(
            conversionFrame, 
            bg=GUI.backgroundColor, 
            fg=GUI.textColor, 
            insertbackground=GUI.buttonColor, 
            width=GUI.labelWidth
        )
        amountInputEntry.grid(row=1)
        amountInputEntry.insert(INSERT, "1.0")


        convertfromInputLabel: Label = Label(
            conversionFrame, 
            text="Convert From:               ", 
            bg=GUI.backgroundColor, 
            fg=GUI.textColor
        ).grid(row=2)
        convertFromInputEntry: Entry = Entry(
            conversionFrame, 
            bg=GUI.backgroundColor, 
            fg=GUI.textColor, 
            insertbackground=GUI.buttonColor,
            width=GUI.labelWidth,
        )
        convertFromInputEntry.grid(row=3)
        convertFromInputEntry.insert(INSERT, Constants.defaultFrom.upper())


        convertToInputLabel: Label = Label(
            conversionFrame, 
            text="Convert To:                     ", 
            bg=GUI.backgroundColor, 
            fg=GUI.textColor
        ).grid(row=4)
        convertToInputEntry: Entry = Entry(
            conversionFrame, 
            bg=GUI.backgroundColor, 
            fg=GUI.textColor, 
            insertbackground=GUI.buttonColor,
            width=GUI.labelWidth
        )
        convertToInputEntry.grid(row=5)
        convertToInputEntry.insert(INSERT, Constants.defaultTo.upper())

        ConversionMeta: Callable[[], None] = lambda: self.__CommandMakeConversion(
            amountInputEntry.get(),
            convertFromInputEntry.get(),
            convertToInputEntry.get()
        )

        Button(
            conversionFrame, 
            text="Make Conversion", 
            command=ConversionMeta, 
            bg=GUI.buttonColor, 
            fg=GUI.textColor,
            width=GUI.buttonWidth
        ).grid(row=6, pady=GUI.buttonYPadding)
    
    def __ComponentUtilityView(self, content: str) -> None:
        utilityFrame: Frame = Frame(master=self.__master)
        utilityFrame.place(
            x=GUI.utilityXOffset, 
            y=GUI.utilityYOffset
        )
        utilityContent: Text = Text(
            master=utilityFrame,
            bg=GUI.backgroundColor, 
            fg=GUI.textColor,
            height=GUI.utilityContentHeight,
            width=GUI.utilityContentWidth
        )
        utilityContent.insert(INSERT, content)
        utilityContent.config(state=DISABLED)
        utilityContent.pack()


    def __CommandMakeConversion(self, amount: str, fromEntry: str, toEntry: str) -> None:
        errorString: str = ""
        resultString: str = ""
        cAmount: float = CheckAmountInputValue(entry=amount)
        cFrom: Union[bool, str] = CheckConversionInputValues(entry=fromEntry, isFromRate=True)
        cTo: Union[bool, str] = CheckConversionInputValues(entry=toEntry, isFromRate=False)
        if not cFrom: 
            errorString += "\nFrom '%s' not found\n" % fromEntry
        if not cTo:
            errorString += "\nTo '%s' not found\n" % toEntry
        if not cAmount:
            errorString += "\n'%s' is not a valid number\n" % amount
        if len(errorString) <= 0 and isinstance(cFrom, str) and isinstance(cTo, str):
            conversion: float = self.__pyrates.Convert(fromRate=cFrom, toRate=cTo, amount=cAmount)
            self.__ComponentUtilityView(content=GenerateConversionString(cFrom, cTo, cAmount, conversion))
        else:
            self.__ComponentUtilityView(content=errorString)

    def __CommandUpdateRates(self) -> None:
        if not self.__pyrates.UpdateRates():
            self.__ComponentUtilityView(content=GenerateUpdateErrorString(self.__pyrates.GetTimestamp()))
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
        result: str = ""
        code: str
        name: str
        for code, name in Constants.currencies.items():
            result += f"{code.upper()}  - {name.title()}\n"
        return result

    @staticmethod
    def Run() -> None:
        root: Tk = Tk()
        root.title(GUI.title)
        if not GUI.resizeable:
            root.resizable(False, False)
        PyRatesGUI(root)
        root.mainloop()

def CheckConversionInputValues(entry: str, isFromRate: bool) -> Union[bool, str]:
    if entry == "":
        if isFromRate:
            return Constants.defaultFrom
        else:
            return Constants.defaultTo
    keys, values = [i.upper() for i in Constants.currencies.keys()], [j.upper() for j in Constants.currencies.values()]
    keys.append(Constants.defaultFrom.upper())
    values.append(Constants.defaultFromName.upper())
    if entry.upper() in keys:
        return entry
    i: int
    for i in range(len(values)):
        if entry.upper() == values[i].upper():
            return keys[i]
    return False


def CheckAmountInputValue(entry: str) -> Union[bool, float]:
    if entry == "":
        return Constants.defaultAmount
    amount: str = entry.replace(",", ".")
    if amount.count(".") <= 1:
        try:
            return float(amount)
        except ValueError as e:
            print(e)
    return False


def GenerateConversionString(cFrom: str, cTo: str, cAmount: float, result: float) -> str:
    sFrom: str
    sTo: str
    if cFrom.upper() == Constants.defaultFrom.upper():
        sFrom = Constants.defaultFromName.upper()
    else:
        sFrom = Constants.currencies[cFrom.upper()].upper()
    if cTo.upper() == Constants.defaultFrom.upper():
        sTo = Constants.defaultFromName.upper()
    else:
        sTo = Constants.currencies[cTo.upper()].upper()
    return f"""CONVERSION:

{cAmount} {sFrom} -> {round(result, 4)} {sTo}
"""

def GenerateUpdateErrorString(timestamp: float) -> str:
    currentAge = abs(time() - timestamp)
    limitAge = abs(Constants.cacheLimitInSeconds - currentAge)
    return f"""
Update of Rates Failed.

Rates are {datetime.utcfromtimestamp(currentAge).strftime('%M')} minutes old
They can be updated again in {datetime.utcfromtimestamp(limitAge).strftime('%M')} minutes
"""
