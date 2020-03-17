# PyRates Docs

* ## [Module Usage](#anchor-pyrates)
  - [`Convert()`](#anchor-pyrates-convert)
  - [`GetRates()`](#anchor-pyrates-get-rates)
  - [`GetRate()`](#anchor-pyrates-get-rate)
  - [`GetRateObjects()`](#anchor-pyrates-get-rate-objects)
  - [`GetRateObject()`](#anchor-pyrates-get-rate-object)
  - [`GetTimestamp()`](#anchor-pyrates-get-timestamp)
  - [`GetTimeString()`](#anchor-pyrates-get-time-string)
  - [`UpdateRates()`](#anchor-pyrates-update-rates)
  - [`__repr__()`](#anchor-pyrates-repr)
* ## [CLI/GUI Usage](#anchor-cli-gui)

<br/><br/>

Module Usage <a name="anchor-pyrates"></a>
================
```python
from pyrates import PyRates

pyrates = PyRates()
```
#### `pyrates.Convert(fromRate, toRate, amount) -> float` <a name="anchor-pyrates-convert"></a>

| Arguments | Type             | Required | Default |
|-----------|------------------|----------|---------|
| fromRate  | Union[str, Rate] | No       | "eur"   |
| toRate    | Union[str, Rate] | No       | "usd"   |
| amount    | float            | No       | 1.0     |
```python
>>> pyrates.Convert(fromRate="nok", toRate="aud", amount=122.5)
19.574542061193018
```
#### `pyrates.GetRates() -> Sequence[Mapping[str, Union[str, float]]]` <a name="anchor-pyrates-get-rates"></a>
```python
>>> pyrates.GetRates()
[...
    },
    {
        "name": "British Pound",
        "currency_code": "GBP",
        "from_euro": 0.901865,
        "to_euro": 1.108813
    },
...]
```
#### `pyrates.GetRate(rate) -> Optional[Mapping[str, Union[str, float]]]` <a name="anchor-pyrates-get-rate"></a>
| Arguments | Type             | Required | Default |
|-----------|------------------|----------|---------|
| rate      | str              | Yes      |    -    |
```python
>>> pyrates.GetRate(rate="dkk")
{
    "name": "Danish Krone", 
    "currency_code": "DKK", 
    "from_euro": 7.473825, 
    "to_euro": 0.1338
}
```
#### `pyrates.GetRateObjects() -> Sequence[Rate]` <a name="anchor-pyrates-get-rate-objects"></a>
```python
>>> pyrates.GetRateObjects()
[...
    <pyrates.rate.rate.Rate object>
...]
```
#### `pyrates.GetRateObject(rate) -> Optional[Rate]` <a name="anchor-pyrates-get-rate-object"></a>
| Arguments | Type             | Required | Default |
|-----------|------------------|----------|---------|
| rate      | str              | Yes      |    -    |
```python
>>> pyrates.GetRateObject(rate="dkk")
<pyrates.rate.rate.Rate object>
```
#### `pyrates.GetTimestamp() -> float` <a name="anchor-pyrates-get-timestamp"></a>
```python
>>> pyrates.GetTimestamp()
1584304647.245822
```
#### `pyrates.GetTimeString() -> str` <a name="anchor-pyrates-get-time-string"></a>
```python
>>> pyrates.GetTimeString()
'2020-03-15 20:37:27 UTC'
```
#### `pyrates.UpdateRates() -> bool` <a name="anchor-pyrates-update-rates"></a>
```python
>>> pyrates.UpdateRates()
True
```
#### `pyrates.GetSupportedCurrencies() -> Mapping[str, str]` <a name="anchor-pyrates-get-supported-currencies"></a>
```python
>>> pyrates.GetSupportedCurrencies()
{
    ...
    "GBP": "British Pound",
    "USD": "US Dollar",
    ...
}
```
#### `pyrates.__repr__() -> str` <a name="anchor-pyrates-repr"></a>
```python
>>> print(pyrates)
'''
SOURCE: x-rates.com
TIME  : 2020-03-15 20:53:20 UTC

|==========================================================================|
| CURRENCY | 1.0 EUR                        | INV 1.0 EUR
|==========================================================================|
| [...]    | [...]                          | [...]
|==========================================================================|
| DKK      | 7.473316                       | 0.133809
|==========================================================================|
| HKD      | 8.599625                       | 0.116284
|==========================================================================|
| HUF      | 339.243118                     | 0.002948
|==========================================================================|
| [...]    | [...]                          | [...]
|==========================================================================|
'''
```

<br/><br/>

CLI/GUI Usage <a name="anchor-cli-gui"></a>
================
Work In Progress

