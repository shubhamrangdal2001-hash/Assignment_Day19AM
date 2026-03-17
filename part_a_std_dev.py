# Part A - Question 4
# Standard deviation computed manually, then verified with NumPy

import math
import numpy as np

def compute_std_dev(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    return math.sqrt(variance)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60]

    custom_std = compute_std_dev(numbers)
    numpy_std = np.std(numbers)   # population std dev by default

    print("Data            :", numbers)
    print(f"Custom Std Dev  : {custom_std:.6f}")
    print(f"NumPy Std Dev   : {numpy_std:.6f}")
    print(f"Results Match   : {abs(custom_std - numpy_std) < 1e-9}")
