from typing import List

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    return sum(num * num for num in even_int_list)