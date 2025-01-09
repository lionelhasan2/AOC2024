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
        rule = rule.split('|')  # Split each rule string by the '|' character
        key = int(rule[0])  # Convert the first part of the split string to an integer (this is the key)
        value = int(rule[1].strip())  # Convert the second part of the split string to an integer (this is the value), after stripping any whitespace
        
        if key not in rules:  # Check if the key does not exist in the dictionary
            rules[key] = value  # If it does not exist, set the dictionary entry to the value
        else:
            if isinstance(rules[key], list):  # Check if the dictionary entry is already a list
                rules[key].append(value)  # If it is a list, append the new value to the list
            else:
                rules[key] = [rules[key], value]  # If it is not a list, create a list with the existing value and the new value

    sum_of_mid_pages = 0  # Initialize a variable to store the sum of the middle pages
    all_pages_good = True  # Initialize a variable to store whether all pages are good
    # Check if any of the page's violate a rule by having a page printed before its prerequisite
    for pages in manual:
        pages = list(map(int, pages.split(',')))  # Split and convert to integers in one step
        all_pages_good = all(
            not (pages[i] in rules and any(pages[j] in rules and pages[i] in rules[pages[j]] for j in range(i + 1, len(pages))))
            for i in range(1, len(pages))
        )
        if all_pages_good:
            sum_of_mid_pages += pages[len(pages) // 2]
    print(sum_of_mid_pages)  # Print the sum of the middle pages


if __name__ == "__main__":
    main()
