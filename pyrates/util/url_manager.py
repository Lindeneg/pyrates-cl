from typing import Tuple, Mapping, Optional, IO, Callable, Union, Any
from time import sleep

from requests import get, RequestException, Response

from pyrates.util.constants import Types, Constants
from pyrates.logger.logger import mLogger


def URLManager(url: str, header: Mapping[str, str], mSleep: int = 8, rJSON: bool = False) -> Types.URLResponse:
    """
    Manages HTTP/HTTPS connections

        Returns:
                result (URLResponse)  : Returns response content on success
    """
    e: RequestException
    try:
        req: Response = get(url=url, params=header)
    except RequestException as e:
        mLogger.critical(e)
        raise RequestException(e)
    status: int = req.status_code
    if status == 200:
        if rJSON:
            return req.json()
        return req.content
    else:
        mLogger.critical(f"URLManager: non-200 response: {req}")
    raise Exception("PyRatesURLError: Failed communication with server. Check '%s/%s' for further inspection." % (Constants.logPath, Constants.logFileName))
