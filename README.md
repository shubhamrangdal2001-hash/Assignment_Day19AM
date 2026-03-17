# Assignment – Week 04 · Day 19 (AM Session)

**PG Diploma · AI-ML & Agentic AI Engineering · IIT Gandhinagar**

**Topics:** Python Fundamentals (Loops, Higher-Order Functions, List Comprehension) · Statistics (Descriptive Statistics, Hypothesis Testing)

---

## 📁 Folder Structure

```
├── part_a_loops.py       # Mean, Median, Variance using loops
├── part_a_hof.py         # Mean, Median, Variance using map/filter/reduce
├── part_a_grades.py      # Filter above-average students + grade assignment
├── part_a_std_dev.py     # Standard deviation (manual + NumPy verification)
├── part_a_groups.py      # Group A & B descriptive stats + difference in means
├── part_b_ttest.py       # Two-sample t-test implemented from scratch
├── part_c_q2.py          # Flatten nested list + remove even numbers
└── README.md
```

---

## ▶️ How to Run

Make sure Python 3 is installed along with the required libraries.

### Install dependencies
```bash
pip install numpy scipy
```

### Run individual files
```bash
python3 part_a_loops.py
python3 part_a_hof.py
python3 part_a_grades.py
python3 part_a_std_dev.py
python3 part_a_groups.py
python3 part_b_ttest.py
python3 part_c_q2.py
```

---

## 📝 Part-wise Description

### Part A — Concept Application

| File | What it does |
|------|-------------|
| `part_a_loops.py` | Computes mean, median, and variance using `for` loops |
| `part_a_hof.py` | Rewrites the same using `map`, `reduce` from `functools` |
| `part_a_grades.py` | Filters students scoring above average and assigns A/B/C grades via list comprehension |
| `part_a_std_dev.py` | Custom standard deviation function, result verified against `np.std()` |
| `part_a_groups.py` | Computes mean, variance, and difference in means for groups A and B |

### Part B — Stretch Problem

| File | What it does |
|------|-------------|
| `part_b_ttest.py` | Implements `two_sample_t_test()` from scratch using Welch's t-test. Computes t-statistic, degrees of freedom, p-value, and prints the conclusion at alpha = 0.05 |

### Part C — Interview Ready

| File | What it does |
|------|-------------|
| `part_c_q2.py` | Flattens a nested list and removes all even numbers using list comprehension |

> Written answers for Q1 (loops vs list comprehension vs HOFs) and Q3 (hypothesis testing concepts) are in the assignment document.

---

## 📊 Sample Outputs

**part_a_groups.py**
```
Group A : [12, 23, 3, 34, 45, 56, 5]
  Mean     : 25.4286
  Variance : 356.8163

Group B : [12, 1, 3, 1, 1, 2, 3, 4, 5, 3, 4]
  Mean     : 3.5455
  Variance : 8.7934

Difference in Means (A - B) : 21.8831
```

**part_b_ttest.py**
```
=============================================
         Two-Sample T-Test Results
=============================================
t-statistic        : 2.8169
Degrees of Freedom : 6.18
p-value            : 0.0295
Significance Level : 0.05
---------------------------------------------
Decision  : Reject H0
Conclusion: The two samples are significantly different.
=============================================
```

**part_c_q2.py**
```
Original nested list : [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
After flattening     : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
After removing evens : [1, 3, 5, 7, 9]
```

---

## 🛠️ Dependencies

- Python 3.x
- `numpy`
- `scipy`

---


