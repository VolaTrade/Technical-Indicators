# C-Optimized Technical Indicator Functions
![PyPI](https://img.shields.io/pypi/v/cython-indicators)

## Authors
@epociask
@rjthompson2
@a-drain

## Installation

### Install from PyPi
```Shell
pip install cython-indicators
```

### Build from Source
1. Clone repository
1. `python setup.py build` to build
1. `python setup.py install --user` to install




## Currently Supported Indicators
- BB - [Bolinger Bands](https://www.investopedia.com/articles/technical/102201.asp)

- EMA -[Exponential Moving Average](https://www.investopedia.com/terms/e/ema.asp)

- FIB - [Upper Fibonacci Retracement Levels](https://www.investopedia.com/terms/f/fibonacciretracement.asp)

- FIB_BB - [Fibonacci Bolinger Bands](https://www.motivewave.com/studies/bollinger_bands_fib_ratios.htm)

- SMA - [Simple Moving Average](https://www.investopedia.com/terms/s/sma.asp)

- WMA - [Weighted Moving Average](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/wma)

- SDV - [Standard Deviation](https://www.mathsisfun.com/data/standard-deviation-formulas.html)

- MOM - [Momentum](https://www.investopedia.com/investing/momentum-and-relative-strength-index/)

## How to Use

```python
import indicators
import numpy as np

closes = np.array([12.3, 11.5, 23.5, 24.2, 32.4])

print(indicators.SMA(closes, 4))

```
`> 22.9`


## Currently Supported and Tested on

-  MACOSX


## To deploy a new version
contact @a-drain or @epociask
