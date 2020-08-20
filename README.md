# apoor

![PyPI - Status](https://img.shields.io/pypi/status/apoor)
![PyPI](https://img.shields.io/pypi/v/apoor)
[![Build Status](https://travis-ci.org/a-poor/apoor.svg?branch=master)](https://travis-ci.org/a-poor/apoor) 
[![codecov](https://codecov.io/gh/a-poor/apoor/branch/master/graph/badge.svg)](https://codecov.io/gh/a-poor/apoor)
![PyPI - License](https://img.shields.io/pypi/l/apoor)


_created by Austin Poor_

A small personal package written in Python with reusable code. 

I created this package to store some of the functions I find myself frequently rewriting.

## Installation Instructions

```bash
$ pip install apoor
```

## Functions

The function `make_scale` returns a function to map a number from a domain to a range.

```
>>> import apoor
>>> scale = apoor.make_scale(0,1,0,10)
>>> scale(0.1)
1.0
>>> scale(0.9)
9.0
```

