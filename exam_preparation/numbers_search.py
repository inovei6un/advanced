import collections
import sys


def numbers_searching(*args):
    num_list = list(args)
    final_list = []
    missing_num = 0
    biggest_number = -sys.maxsize
    lowest_number = sys.maxsize
    for num in num_list:
        if num > biggest_number:
            biggest_number = num
        if num < lowest_number:
            lowest_number = num
    for number in range(lowest_number, biggest_number + 1):
        if number not in num_list:
            final_list.append(number)
    duplicate_list = [item for item, count in collections.Counter(num_list).items() if count > 1]
    final_list.append(sorted(duplicate_list))
    return final_list


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))