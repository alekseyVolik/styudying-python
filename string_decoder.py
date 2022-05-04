"""
        In this module you find function that solves
task (link: https://stepik.org/lesson/3363/step/2?unit=1135)
from python education course
"""
from re import findall
from os.path import dirname, join
from typing import Callable


def string_decoder(decode_string: str) -> str:
    nums = findall(r'\d+', decode_string)
    letters = findall(r'\D', decode_string)
    return ''.join(int(num) * letter for num, letter in zip(nums, letters))


def decode_file(file_name: str, decode_func: Callable[[str], str]) -> None:
    file_path_source = join(dirname(__file__), 'static', file_name)
    file_path_result = join(dirname(__file__), 'static', 'decode_result.txt')
    with open(file_path_source, 'r') as source_file, open(file_path_result, 'w') as result_file:
        result_file.write(decode_func(source_file.read()))


if __name__ == '__main__':
    decode_file('dataset_3363_2.txt', string_decoder)
