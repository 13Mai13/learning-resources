import pathlib
import numpy as np


def read_file():
    path = pathlib.Path().absolute()
    print(path)
    quizzes = np.zeros((49, 81), np.int32)
    solutions = np.zeros((49, 81), np.int32)
    for i, line in enumerate(
        open(
            f"{path}/content/projects/sudoku-project/sudoku_first_50_examples.csv", "r"
        )
        .read()
        .splitlines()[1:]
    ):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
    quizzes = quizzes.reshape((-1, 9, 9))
    solutions = solutions.reshape((-1, 9, 9))
    return quizzes, solutions
