"""
        In this module you find function that solves
task (link: https://stepik.org/lesson/3363/step/4?unit=1135)
from python education course
"""
from os.path import dirname, join


def student_score_statistic(file_name):
    statistic_file_path = join(dirname(__file__), 'static', file_name)
    report_file_path = join(dirname(__file__), 'static', 'student statistic report.txt')
    with open(statistic_file_path, 'r') as statistic_file, open(report_file_path, 'w') as report_file:
        total_math, total_phys, total_lang, i = 0, 0, 0, 0
        for student_data in statistic_file.readlines():
            print(student_data.strip().split(';'))
            scores = [int(score) for score in student_data.strip().split(';') if score.isdigit()]
            average_scores = sum(scores) / len(scores)
            print(scores)
            total_math += scores[0]
            total_phys += scores[1]
            total_lang += scores[2]
            i += 1
            print(average_scores, file=report_file)
        print(total_math / i, total_phys / i, total_lang / i, file=report_file)
