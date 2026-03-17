# Part A - Question 5
# Compute mean, variance, and difference in means for groups A and B

def compute_mean(data):
    return sum(data) / len(data)

def compute_variance(data):
    mean = compute_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


if __name__ == "__main__":
    A = [12, 23, 3, 34, 45, 56, 5]
    B = [12, 1, 3, 1, 1, 2, 3, 4, 5, 3, 4]

    mean_a = compute_mean(A)
    mean_b = compute_mean(B)
    var_a  = compute_variance(A)
    var_b  = compute_variance(B)

    print(f"Group A : {A}")
    print(f"  Mean     : {mean_a:.4f}")
    print(f"  Variance : {var_a:.4f}")

    print(f"\nGroup B : {B}")
    print(f"  Mean     : {mean_b:.4f}")
    print(f"  Variance : {var_b:.4f}")

    print(f"\nDifference in Means (A - B) : {mean_a - mean_b:.4f}")
