PyRates
=============
Work-In-Progress
---------
- Implement GUI and CLI

# Installation

```shell
$ python -m pip install pyrates-cl
```

# Usage

```python
>>> from pyrates import PyRates

>>> pyrates = PyRates()


"""
Optional Args

fromRate: str   - default = "eur"
toRate  : str   - default = "usd"
amount  : float - default = 1


return  : float
"""
>>> pyrates.Convert(fromRate="nok", toRate="aud", amount=122.5)
111.17176148320918


"""
return: Sequence[Mapping[str, Union[str, float]]]
"""
>>> pyrates.GetRates()
[...
    {
        "name": "British Pound",
        "currency_code": "GBP",
        "from_euro": 0.906095,
        "to_euro": 1.103637
    }
...]


"""
Optional Arg

rate: str - default = "usd"

return: Optional[Mapping[str, Union[str, float]]]
"""
>>> pyrates.GetRate(rate="dkk")
{
    "name": "Danish Krone", 
    "currency_code": "DKK", 
    "from_euro": 7.488282, 
    "to_euro": 0.133542
}


"""
return: Mapping[str, str]
"""
>>> pyrates.GetSupportedCurrencies()
{
    ...
    "GBP": "British Pound",
    "USD": "US Dollar",
    ...
}


"""
return: float
"""
>>> pyrates.GetTimestamp()
1584247390.485117


"""
return: str
"""
>>> pyrates.GetTimeString()
'2020-03-15 04:43:10 UTC'


>>> print(pyrates)
|==========================================================================|
| CURRENCY | 1.0 EUR                        | INV 1.0 EUR
|==========================================================================|
| [...]    | [...]                          | [...]
|==========================================================================|
| DKK      | 7.488282                       | 0.133542
|==========================================================================|
| HKD      | 8.637966                       | 0.115768
|==========================================================================|
| HUF      | 339.13462                      | 0.002949
|==========================================================================|
| [...]    | [...]                          | [...]
|==========================================================================|
```

