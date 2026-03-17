# Part C - Question 2 (Coding)
# Flatten a nested list and remove all even numbers using list comprehension

def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

def remove_evens(flat_list):
    return [x for x in flat_list if x % 2 != 0]


if __name__ == "__main__":
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]

    print("Original nested list :", nested)

    flat = flatten(nested)
    print("After flattening     :", flat)

    odd_only = remove_evens(flat)
    print("After removing evens :", odd_only)
