# Advent of Code
# Day 3: Ceres Search 
# Author: Lionel Hasan
# Date: 2024-12-04

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    

def main():

    with open("/Users/lionelhasan/AOC2024/Day 4/input-4.txt") as file:
        data = file.read()
        lines = data.split("\n")
    
    total = 0

    position_char_dict = {}
    for line_number, line in enumerate(lines, start=0):
        # For each character in the line, map the the character to a position
        for char_number, char in enumerate(line, start=0):
            position = Position(char_number, line_number)
            position_char_dict[position] = char

        # For each position, check all 8 directions to see if the next 4 characters spell "XMAS"
    for position, char in position_char_dict.items():
        if char == 'X':
            # Check right
            if position.x + 3 < len(lines[position.y]):
                if all(position_char_dict.get(Position(position.x + i, position.y)) == char for i, char in enumerate("XMAS")):
                    total += 1
            # Check left
            if position.x - 3 >= 0:
                if all(position_char_dict.get(Position(position.x - i, position.y)) == char for i, char in enumerate("XMAS")):
                    total += 1
            # Check down
            if position.y + 3 < len(lines):
                if all(position_char_dict.get(Position(position.x, position.y + i)) == char for i, char in enumerate("XMAS")):
                    total += 1
            # Check up
            if position.y - 3 >= 0:
                if all(position_char_dict.get(Position(position.x, position.y - i)) == char for i, char in enumerate("XMAS")):
                    total += 1
            # Check down right
            if position.x + 3 < len(lines[position.y]) and position.y + 3 < len(lines):
                if all(position_char_dict.get(Position(position.x + i, position.y + i)) == char for i, char in enumerate("XMAS")):
                    total += 1
            # Check down left
            if position.x - 3 >= 0 and position.y + 3 < len(lines):
                if all(position_char_dict.get(Position(position.x - i, position.y + i)) == char for i, char in enumerate("XMAS")):
                    total += 1
            # Check up right
            if position.x + 3 < len(lines[position.y]) and position.y - 3 >= 0:
                if all(position_char_dict.get(Position(position.x + i, position.y - i)) == char for i, char in enumerate("XMAS")):
                    total += 1
            # Check up left
            if position.x - 3 >= 0 and position.y - 3 >= 0:
                if all(position_char_dict.get(Position(position.x - i, position.y - i)) == char for i, char in enumerate("XMAS")):
                    total += 1
        
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
