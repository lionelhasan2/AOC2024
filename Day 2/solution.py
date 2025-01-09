# Advent of Code
# Day 1: Red-Nosed Reports
# Author: Lionel Hasan
# Date: 2024-12-02


def isSafeReport(input_values):
    diff_between_one_and_three = all(1 <= abs(a - b) <= 3 for a, b in zip(input_values, input_values[1:]))
    sorted_or_reversed = input_values == sorted(input_values) or input_values == sorted(input_values, reverse=True)
    return diff_between_one_and_three and sorted_or_reversed

def isSafeReport2(input_values):
    for i in range(len(input_values)):
        new_list = input_values[:i] + input_values[i + 1:]
        if isSafeReport(new_list):
            return True
    return False

def main():
    safe_reports1 = 0 # Initialize the number of safe reports (part 1)
    safe_reports2 = 0 # Initialize the number of safe reports (part 2)
# Read input
    with open("/Users/lionelhasan/AOC2024/Day 2/input-2.txt", "r") as file:
        for line in file:
            # iteratively split the line into individual values
            input_values = line.split(" ")
            # convert the values to integers
            input_values = list(map(int, input_values))
            # check if the values are sorted in ascending order
            if isSafeReport(input_values):
                safe_reports1 += 1
            if isSafeReport2(input_values):
                safe_reports2 += 1

    print(f"Safe Reports: {safe_reports1}")
    print(f"Safe Reports: {safe_reports2}")
if __name__ == "__main__":
    main()