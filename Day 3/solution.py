# Advent of Code
# Day 3: Mull It Over 
# Author: Lionel Hasan
# Date: 2024-12-03


def main():
    right_ptr = 0
    left_ptr = 0
    sum = 0
    enabled = True
    with open("/Users/lionelhasan/AOC2024/Day 3/input-3.txt") as file:
        data = file.read()
        while left_ptr < len(data):
            if data[left_ptr:left_ptr+4] == 'mul(':
                right_ptr = left_ptr + 4
                first_num = ''
                if right_ptr < len(data) and data[right_ptr].isdigit() and enabled:
                    while right_ptr < len(data) and data[right_ptr].isdigit():
                        first_num += data[right_ptr]
                        right_ptr += 1
                    if right_ptr < len(data) and data[right_ptr] == ',':
                        right_ptr += 1
                        second_num = ''
                        if right_ptr < len(data) and data[right_ptr].isdigit():
                            while right_ptr < len(data) and data[right_ptr].isdigit():
                                second_num += data[right_ptr]
                                right_ptr += 1
                            if right_ptr < len(data) and data[right_ptr] == ')':
                                sum += int(first_num) * int(second_num)
                                left_ptr = right_ptr + 1
                            left_ptr = right_ptr + 1
                            continue
            elif data[left_ptr:left_ptr+7] == 'don\'t()':
                enabled = False
                left_ptr += 7
                continue
            elif data[left_ptr:left_ptr+4] == 'do()':
                enabled = True
                left_ptr += 4
                continue
            left_ptr += 1
            
    print(f"Sum: {sum}")
            
  


if __name__ == "__main__":
    main()
