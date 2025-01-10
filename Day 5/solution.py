# Advent of Code
# Day 5: Print Queue 
# Author: Lionel Hasan
# Date: 2024-12-05

def main():
    # Read the input file, split the data into lines until an empty line is reached
    with open("/Users/lionelhasan/AOC2024/Day 5/input-5.txt") as file:
        data = file.read().splitlines()
    
    # Find the index of the first empty line
    empty_line_index = data.index('')

    # Split the data into two parts: before the empty line and after the empty line
    rules_list = data[:empty_line_index]
    manual = data[empty_line_index + 1:]

    # Create a dictionary to store the rules
    rules = {}
    for rule in rules_list:
        key, value = map(int, rule.split('|'))  # Split and convert both parts to integers in one step
        if key in rules:
            if not isinstance(rules[key], list):
                rules[key] = [rules[key]]  # Convert to list if not already a list
            rules[key].append(value)  # Append the new value
        else:
            rules[key] = value  # Set the dictionary entry to the value if key does not exist

    sum_of_mid_pages = 0  # Initialize a variable to store the sum of the middle pages
    # Check if any of the page's violate a rule by having a page printed before its prerequisite
    for pages in manual:
        pages = [int(p) for p in pages.split(',')]
        all_pages_good = all(
            not any(pages[i] in rules.get(pages[j], []) for j in range(i + 1, len(pages)))
            for i in range(1, len(pages))
        )
        if all_pages_good:
            sum_of_mid_pages += pages[len(pages) // 2]

    print(sum_of_mid_pages)  # Print the sum of the middle pages


if __name__ == "__main__":
    main()
