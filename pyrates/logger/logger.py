from logging import getLogger, FileHandler, Formatter, DEBUG, Logger
from os import path as oPath

from pyrates.util.constants import Types, Constants

mLogger: Logger = getLogger()
mLogger.setLevel(DEBUG)
fileHandler: FileHandler = FileHandler("%s/%s" % (str(Constants.logPath), Constants.logFileName))
fileFormat: Formatter = Formatter("%(levelname)s | %(asctime)s | %(name)s | %(message)s")
fileHandler.setFormatter(fileFormat)
mLogger.addHandler(fileHandler)
