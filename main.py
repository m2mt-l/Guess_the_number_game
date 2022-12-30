import sys, random

ATTEMPT_NUMBER_HASH = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th"}


def input_min_number():
    min_number = input("Please input a minimum number between 1 and 100: \n")
    if check_int_or_not(min_number) is False:
        return input_min_number()
    min_number = int(min_number)
    if check_range_min_and_max_number(min_number) is False:
        return input_min_number()
    return min_number


def input_max_number(min_number: int):
    max_number = input("Please input a maximum number between 1 and 100: \n")
    if check_int_or_not(max_number) is False:
        return input_max_number(min_number)
    max_number = int(max_number)
    if check_valid_max_number(min_number, max_number) is False:
        return input_max_number(min_number)
    if check_range_min_and_max_number(max_number) is False:
        return input_max_number(min_number)
    return max_number


def main():
    min_number = input_min_number()
    max_number = input_max_number(min_number)
    ans_number = random.randint(min_number, max_number)
    guess_number(ans_number)


def input_guess_number():
    guess_number = input("Please input your guess number: \n")
    return int(guess_number) if check_int_or_not(guess_number) else input_guess_number()


def guess_number(ans_number: int):
    for i in range(1, 5):
        guess_number = input_guess_number()
        if guess_number == ans_number:
            print(f"Correct. Your {str(ATTEMPT_NUMBER_HASH[i])} attempt.")
            return
    print("Fail. Exceeded 5th attempt.")


def check_int_or_not(input: str):
    try:
        int(input)
        return True
    except ValueError:
        print("The input must be a number.")
        return False


def check_range_min_and_max_number(num: int):
    if 1 <= num <= 100:
        return True
    else:
        print("Invalid range. Please input between 1 and 100.")
        return False


def check_valid_max_number(min_num: int, max_num: int):
    if max_num > min_num:
        return True
    else:
        print("The maximum number must be greater than the minimum number.")
        return False


if __name__ == "__main__":
    main()
