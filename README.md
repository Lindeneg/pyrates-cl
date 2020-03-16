PyRates
=============
PyRates supports conversion between 54 currency rates
-------
Can be used as:
- Package/Module
- CLI
- GUI

The rates are fetched by webscraping x-rates.com and saved locally

In order to keep get-requests to a minimum, rates are only updated if they are older than 30 minutes

The base currency is by default: Euro. Work in progress to let the user change the base currency at will

-------------

To do:
- Allow changing of base currency


# Installation

PIP
```shell
$ python -m pip install pyrates-cl
```

Source

```shell
$ git clone https://github.com/Lindeneg/pyrates-cl && cd pyrates-cl
$ python setup.py install
```

#### [Documentation](https://github.com/lindeneg/docs)