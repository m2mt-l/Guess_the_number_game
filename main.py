import sys, random

attempt_number_hash = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th"}


def input_min_number():
    min_number = input("Please input a minimum number: \n")
    return int(min_number) if check_int_or_not(min_number) else input_min_number()


def input_max_number(min_number: int):
    max_number = input("Please input a maximum number: \n")
    if check_int_or_not(max_number):
        max_number = int(max_number)
        if max_number > min_number:
            return max_number
        else:
            print("The maximum number must be greater than the minimum number.")
            return input_max_number(min_number)
    else:
        return input_max_number(min_number)


def input_min_and_max():
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
            print(f"Correct. Your {str(attempt_number_hash[i])} attempt.")
            return
    print("Fail. Exceeded 5th attempt.")


def check_int_or_not(input: str):
    try:
        int(input)
        return True
    except ValueError:
        print("The input must be a number.")
        return False


if __name__ == "__main__":
    input_min_and_max()
