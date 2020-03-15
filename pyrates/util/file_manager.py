from typing import Optional, IO, Callable, Any
from json import dump, load

from pyrates.util.constants import Types, Constants
from pyrates.logger.logger import mLogger


def FileManager(
    path: str, 
    name: str, 
    data: Optional[Types.File] = None
    ) -> Optional[Types.File]:
    """
    Manages reading/writing of local files

    Return File or None

        Returns:
                result (File, None)  : Returns type File if the file could be found
                                       Returns None if the file could not be found or if nothing is being read
    """
    mData: Optional[Types.File] = None
    flag: Callable = lambda i: "w" if i else "r"
    mFile: IO[Any]
    try:
        with open(f"{path}/{name}", flag(data)) as mFile:
            mLogger.debug(f"FileManager: handling ({path}, {name})")
            if data:
                dump(data, mFile)
            else:
                mData = load(mFile)
            mFile.close()
    except FileNotFoundError:
        mLogger.warning(f"FileManager: '{path}/{name}' was not found")
        with open(f"{path}/{name}", "w") as mFile:
            dump(Constants.defaultDict, mFile)
            mFile.close()
    return mData
