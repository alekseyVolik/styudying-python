"""
        In this module you find function that solves
task (link: https://stepik.org/lesson/3363/step/3?unit=1135)
from python education course
"""
from collections import Counter
from os.path import join, dirname


def top_word(line: str):
    sorted_split_words = sorted(line.lower().split())
    top_element = Counter(sorted_split_words).most_common(1)
    return top_element[0]


def top_words_reader(file_name):
    file_path_source = join(dirname(__file__), 'static', file_name)
    with open(file_path_source, 'r') as source_file:
        return top_word(source_file.read())


if __name__ == '__main__':
    print(top_words_reader('dataset_3363_3.txt'))
