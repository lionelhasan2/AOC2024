# Advent of Code
# Day 1: Historian Hysteria
# Puzzle 2
# Author: Lionel Hasan
# Date: 2024-12-01


def main():
    left_list = []
    right_list = []
    right_dict = {} # Use a dictionary to store the right values and their frequencies in one pass
    # Read input
    with open("/Users/lionelhasan/AOC2024/Day 1/input.txt", "r") as file:
        for line in file:
            left, right = line.split("   ")
            left_list.append(int(left))
            right_list.append(int(right))
            if int(right) in right_dict:
                right_dict[int(right)] += 1
            else:
                right_dict[int(right)] = 1
    
    # Calculate the distance (part 1)
    distance = sum(abs(a - b ) for a, b in zip(sorted(left_list), sorted(right_list)))
    print(f"Distance: {distance}")
    # Calculate similarity score (part 2)
    similarity_score = sum(left_list[i] * right_dict.get(left_list[i], 0) for i in range(len(left_list)))
    print(f"Similarity Score: {similarity_score}")

if __name__ == "__main__":
    main()

