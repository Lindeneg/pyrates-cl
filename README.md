PyRates
=============
Work-In-Progress
---------
- Implement GUI and CLI

Convert rates between 53 currencies

# Installation

with pip
```shell
$ python -m pip install pyrates-cl
```

with source

```shell
$ git clone https://github.com/Lindeneg/pyrates-cl && cd pyrates-cl
$ python setup.py install
```

# Usage
```python
from pyrates import PyRates

pyrates = PyRates()
```
```python
# pyrates.Convert(fromRate, toRate, amount)      -> float

"""
| Arguments | Type             | Required | Default |
|-----------|------------------|----------|---------|
| fromRate  | Union[str, Rate] | No       | "usd"   |
| toRate    | Union[str, Rate] | No       | "eur"   |
| amount    | float            | No       | 1.0     |
"""
>>> pyrates.Convert(fromRate="nok", toRate="aud", amount=122.5)
111.17176148320918


# pyrates.GetRates()                             -> Sequence[Mapping[str, Union[str, float]]]
>>> pyrates.GetRates()
[...
    {
        "name": "British Pound",
        "currency_code": "GBP",
        "from_euro": 0.906095,
        "to_euro": 1.103637
    }
...]


# pyrates.GetRate(rate)                         -> Optional[Mapping[str, Union[str, float]]]
"""
| Arguments | Type             | Required | Default |
|-----------|------------------|----------|---------|
| rate      | str              | Yes      |    -    |
"""
>>> pyrates.GetRate(rate="dkk")
{
    "name": "Danish Krone", 
    "currency_code": "DKK", 
    "from_euro": 7.488282, 
    "to_euro": 0.133542
}


# pyrates.GetTimestamp()                        -> float
>>> pyrates.GetTimestamp()
1584247390.485117


# pyrates.GetTimeString()                       -> str
>>> pyrates.GetTimeString()
'2020-03-15 04:43:10 UTC'


# pyrates.GetSupportedCurrencies()              -> Mapping[str, str]
>>> pyrates.GetSupportedCurrencies()
{
    ...
    "GBP": "British Pound",
    "USD": "US Dollar",
    ...
}


# pyrates.__repr__()                            -> str
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