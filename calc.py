# calc.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("деление на ноль")
    return a / b

# test_calc.py

