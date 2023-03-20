from read_files import read_file

"""
[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]
[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8]
[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8]
[3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8]
[4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8]
[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8]
[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8]
[7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8]
[8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8]
"""

quizzes, solutions = read_file()
# import pdb

# pdb.set_trace()


def is_number_subset(number, subset) -> bool:
    """
    Is a integer part of an array.
    """
    is_in_subset = False
    for value in subset:
        if number == value:
            is_in_subset = True
            break
    return is_in_subset


def get_interval(number: int):
    """
    Get an interval given a number.
    """
    if number < 3:
        min_interval = 0
        max_interval = 2
    elif 3 <= number < 6:
        min_interval = 3
        max_interval = 5
    elif 6 <= number <= 8:
        min_interval = 6
        max_interval = 8
    return min_interval, max_interval


def get_number_grid(i, j, matrix):
    """
    Given one position, determine it's grid.
    """
    i_min, i_max = get_interval(i)
    j_min, j_max = get_interval(j)

    return matrix[i_min:i_max, j_min:j_max]

def is_number_in_grid(i, j, matrix, number):
    """
    Given a position and a number check if the number is on the grid.
    """
    grid = get_number_grid(i, j, matrix)
    return is_number_subset(number, grid.flatten())

def get_candidate_numbers(i, j, matrix):
    """
    Return a list with all the candidate numbers for a position
    """
    candidate_number_list = []
    for candidate_number in range(10):
        not_in_row = not is_number_subset(candidate_number, matrix[i, :])
        not_in_colum = not is_number_subset(candidate_number, matrix[:, j])
        not_in_subset = not is_number_in_grid(i, j, matrix, candidate_number)
        if not_in_row & not_in_colum & not_in_subset:
            candidate_number_list.append(candidate_number)
    return candidate_number_list

def is_matrix_incomplete(matrix):
    # import pdb
    # pdb.set_trace()
    return is_number_subset(0, matrix.flatten())

def solve(matrix):
    # TODO: Infinity loop when guessing is compulsory
    # TODO: Not working as expected
    while is_matrix_incomplete(matrix):
        for i in range(9):
            for j in range(9):
                if matrix[i, j] == 0:
                    candidate_numbers = get_candidate_numbers(i, j, matrix)
                    if len(candidate_numbers) == 1:
                        matrix[i, j] = candidate_numbers[0]
                        break
    print(f"There is no alternative with a single alternative number")
    print(f"This is an infinite loop")
    return(matrix)



for position, quizz in enumerate(quizzes):

    solution = solve(quizzes[position])
    print(solution, solutions[position])
    # import pdb 
    # pdb.set_trace()
    comparison = solution == solutions[position]
    print(f"Are both solution equal: {comparison.flatten().all()}")