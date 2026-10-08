# Pandas and NumPy Assignment

This repository contains my solutions for **NeuralAI Panel 5 - Test 01 of Pandas and NumPy**.

## Repository structure

- `numpy/` contains five NumPy programs.
- `pandas/` contains five Pandas programs.

## Requirements

- Python 3
- NumPy
- Pandas

Install the required libraries using:

```bash
pip install numpy pandas
```

## How to run

Run any file from the repository root. For example:

```bash
python numpy/q1_array_manipulation.py
python pandas/q1_dataframe_basics.py
```

Each file is a complete program for one question of the assignment.

## Important note for NumPy Q4

After the bias column is added, the columns of the given matrix are linearly dependent. Therefore, `X.T @ X` is singular and does not have a normal inverse. NumPy's `np.linalg.pinv()` is used as the correct alternative for calculating the regression weights.
