# Part A - Question 1
# Computing Mean, Median, and Variance using loops

def compute_mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def compute_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def compute_variance(data):
    mean = compute_mean(data)
    total = 0
    for x in data:
        total += (x - mean) ** 2
    return total / len(data)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60]

    print("Data:", numbers)
    print(f"Mean     : {compute_mean(numbers)}")
    print(f"Median   : {compute_median(numbers)}")
    print(f"Variance : {compute_variance(numbers):.4f}")
