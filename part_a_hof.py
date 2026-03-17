# Part A - Question 2
# Computing Mean, Median, and Variance using Higher-Order Functions (map, filter, reduce)

from functools import reduce

def compute_mean_hof(data):
    # reduce to sum all elements, then divide
    total = reduce(lambda acc, x: acc + x, data)
    return total / len(data)

def compute_median_hof(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]

def compute_variance_hof(data):
    mean = compute_mean_hof(data)
    # map each element to its squared deviation
    squared_diffs = list(map(lambda x: (x - mean) ** 2, data))
    # reduce to get the sum, then divide
    return reduce(lambda acc, x: acc + x, squared_diffs) / len(data)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60]

    print("Data:", numbers)
    print(f"Mean (HOF)     : {compute_mean_hof(numbers)}")
    print(f"Median (HOF)   : {compute_median_hof(numbers)}")
    print(f"Variance (HOF) : {compute_variance_hof(numbers):.4f}")
