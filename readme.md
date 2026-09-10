# 42-Matrix

**42-Matrix** is a project aimed at implementing a matrix calculation library in **Python**, adhering to strict constraints and covering the entire subject (bonus included).

## Overview

This project provides tools for manipulating **vectors**, **matrices**, and **complex numbers**, as well as associated calculation functions (products, projections, algebraic operations, etc.).

The architecture is designed to clearly separate:
- **mathematical classes**
- **utility and calculation functions**
- **test scripts** for each exercise

## Features

* Full implementation of mandatory exercises + bonus exercises
* Dedicated classes for:
  * Vectors
  * Matrices
  * Complex numbers
* Calculation functions separated from classes
* Independent test scripts for each exercise
* Modular and easily reusable code

## Project Structure

```text
.
├── classes/
│   ├── __init__.py
│   ├── Complex.py
│   ├── Matrix.py
│   └── Vector.py
│
├── functions/
│   ├── __init__.py
│   ├── calculations.py
│   ├── projection.py
│   └── vector_calc.py
│
├── test_mains/
│   ├── Ex00.py
│   ├── Ex01.py
│   ├── ...
│   └── Ex15.py
│
├── en.subject.pdf
└── readme.md
```