def calibration_finder(value: str) -> int:
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    value_digits = [char for char in value if char in digits]

    if len(value_digits) == 1:
        return int(value_digits[0]+value_digits[0])
    else:
        return int(value_digits[0]+value_digits[-1])
    
def calibration_finder_2(value:str) -> int:
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    digits_spelled = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    

    


# def find_sum() -> int:
#     with open ('Advent_of_Code/day_one/lib/calibration_codes.txt', 'r') as f:
#         lines = [line for line in f]
#         values_list = [calibration_finder(line) for line in lines]
#         return sum(values_list)
    

# print(find_sum())