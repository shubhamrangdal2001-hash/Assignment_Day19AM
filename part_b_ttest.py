# Part B - Stretch Problem
# Two-sample t-test implemented from scratch

import math
from scipy import stats

def compute_mean(data):
    return sum(data) / len(data)

def compute_sample_variance(data):
    # using n-1 for sample variance (Bessel's correction)
    mean = compute_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def two_sample_t_test(sample1, sample2, alpha=0.05):
    n1, n2   = len(sample1), len(sample2)
    mean1    = compute_mean(sample1)
    mean2    = compute_mean(sample2)
    var1     = compute_sample_variance(sample1)
    var2     = compute_sample_variance(sample2)

    # standard error of the difference
    se = math.sqrt(var1 / n1 + var2 / n2)

    # t-statistic
    t_stat = (mean1 - mean2) / se

    # Welch's degrees of freedom approximation
    numerator = (var1 / n1 + var2 / n2) ** 2
    denominator = ((var1 / n1) ** 2) / (n1 - 1) + ((var2 / n2) ** 2) / (n2 - 1)
    df = numerator / denominator

    # two-tailed p-value
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=df))

    print("=" * 45)
    print("         Two-Sample T-Test Results")
    print("=" * 45)
    print(f"Sample 1 : Mean = {mean1:.4f}, Var = {var1:.4f}, n = {n1}")
    print(f"Sample 2 : Mean = {mean2:.4f}, Var = {var2:.4f}, n = {n2}")
    print(f"t-statistic         : {t_stat:.4f}")
    print(f"Degrees of Freedom  : {df:.2f}")
    print(f"p-value             : {p_value:.4f}")
    print(f"Significance Level  : {alpha}")
    print("-" * 45)
    if p_value < alpha:
        print("Decision  : Reject H0")
        print("Conclusion: The two samples are significantly different.")
    else:
        print("Decision  : Fail to reject H0")
        print("Conclusion: No significant difference between samples.")
    print("=" * 45)

    return t_stat, p_value


if __name__ == "__main__":
    A = [12, 23, 3, 34, 45, 56, 5]
    B = [12, 1, 3, 1, 1, 2, 3, 4, 5, 3, 4]

    two_sample_t_test(A, B)
