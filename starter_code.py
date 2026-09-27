"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    """
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])

# Uncomment to test sum_list
print("\nTest sum_list:")
print(f"  sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])} (expected: 10)")
print(f"  sum_list([]) = {sum_list([])} (expected: 0)")
print(f"  sum_list([5, 5, 5]) = {sum_list([5, 5, 5])} (expected: 15)")


def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    """
    if len(numbers) == 0:
        return 0

    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])
    else:
        return count_even(numbers[1:])

# Uncomment to test count_even
print("\nTest count_even:")
print(f"  count_even([1, 2, 3, 4, 5, 6]) = {count_even([1, 2, 3, 4, 5, 6])} (expected: 3)")
print(f"  count_even([1, 3, 5]) = {count_even([1, 3, 5])} (expected: 0)")
print(f"  count_even([2, 4, 6]) = {count_even([2, 4, 6])} (expected: 3)")

def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    """
    if len(strings) == 0:
        return []

    rest = find_strings_with(strings[1:], target)

    if target in strings[0]:
        return [strings[0]] + rest
    else:
        return rest

# Uncomment to test find_strings_with
print("\nTest find_strings_with:")
result = find_strings_with(["hello", "world", "help", "test"], "hel")
print(f"  find_strings_with(['hello', 'world', 'help', 'test'], 'hel') = {result}")
print(f"  (expected: ['hello', 'help'])")
    
result = find_strings_with(["cat", "dog", "bird"], "z")
print(f"  find_strings_with(['cat', 'dog', 'bird'], 'z') = {result}")
print(f"  (expected: [])")

# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    """
    if os.path.isfile(directory_path):
        return 1

    count = 0

    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            count += 1
        elif os.path.isdir(full_path):
            count += count_files(full_path)

    return count


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    """
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        return []

    infected_files = []

    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            if full_path.endswith(extension):
                infected_files.append(full_path)

        elif os.path.isdir(full_path):
            infected_files.extend(find_infected_files(full_path, extension))

    return infected_files


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================


if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE")
    print("Complete the functions above, then run this file to test your work.\n")
    
    ## 1. Uncomment to run tests for count_files functions
    print("Total files (Test Case 1):", count_files("test_cases/case1_flat")) # 5
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested")) # 4
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected")) # 5

    ## 2. Uncomment to run count_files for breached files
    print("Total files (breeched files):", count_files("breach_data")) # ???

    ## 3. Uncomment to run tests for find_infected_files function
    print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case1_flat"))) # 0
    print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case2_nested"))) # 0
    print("Total Infected Files (Test Case 3):", len(find_infected_files("test_cases/case3_infected"))) # 3

    ## 4. Uncomment to run find_infected breached files
    print("Total Infected Files (breached files):", len(find_infected_files("breach_data"))) # ???

    ## 5. Determine how many files were corrupted in each generated department folder
    print("Creative infected files:", len(find_infected_files("breach_data/Creative")))
    print("Marketing infected files:", len(find_infected_files("breach_data/Marketing")))
    print("Marketing_1 infected files:", len(find_infected_files("breach_data/Marketing_1")))
    print("Sales infected files:", len(find_infected_files("breach_data/Sales")))
    print("Sales_1 infected files:", len(find_infected_files("breach_data/Sales_1")))

    
    print("\n⚠ Uncomment the test functions in the main block to run tests!")