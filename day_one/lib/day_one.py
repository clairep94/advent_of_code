def calibration_finder(value: str) -> str:
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    value_digits = [char for char in value if char in digits]

    if len(value_digits) == 1:
        return int(value_digits[0]+value_digits[0])
    else:
        return int(value_digits[0]+value_digits[-1])
    

