from collections import deque
from enum import Enum


class Color(Enum):
    BLACK = '#'
    WHITE = '.'

    def __str__(self):
        return self.value


def matrix_to_string(m):
    str_value = ""

    for single_row in m:
        for color in single_row:
            str_value += str(color)

        str_value += '\n'

    return str_value


def flip_color(matrix, row, col):
    """
    time: O(N^2)
    space: O(1)
    """
    new_color = Color.WHITE

    if matrix[row][col] == Color.WHITE:
        new_color = Color.BLACK

    if matrix[row][col] == new_color:
        return

    data = deque()
    data.append((row, col))

    while data:
        cur_row, cur_col = data.popleft()

        matrix[cur_row][cur_col] = new_color

        check_position(matrix, cur_row + 1, cur_col, data, new_color)
        check_position(matrix, cur_row - 1, cur_col, data, new_color)

        check_position(matrix, cur_row, cur_col + 1, data, new_color)
        check_position(matrix, cur_row, cur_col - 1, data, new_color)


def check_position(matrix, row, col, working_queue, new_color):
    # out of matrix boundary
    if row < 0 or row == len(matrix) or col < 0 or col == len(matrix[row]):
        return

    # same color, skip
    if matrix[row][col] == new_color:
        return

    working_queue.append((row, col))


def main():
    m_size = 10
    m = [[Color.WHITE for _ in range(m_size)] for _ in range(m_size)]

    m[0][0] = Color.BLACK
    m[0][2] = Color.BLACK
    m[0][6] = Color.BLACK
    m[0][7] = Color.BLACK
    m[0][8] = Color.BLACK
    m[0][9] = Color.BLACK

    m[1][2] = Color.BLACK
    m[1][5] = Color.BLACK
    m[1][8] = Color.BLACK
    m[1][9] = Color.BLACK

    m[2][0] = Color.BLACK
    m[2][1] = Color.BLACK
    m[2][2] = Color.BLACK
    m[2][5] = Color.BLACK
    m[2][6] = Color.BLACK
    m[2][8] = Color.BLACK
    m[2][9] = Color.BLACK

    m[3][1] = Color.BLACK
    m[3][3] = Color.BLACK
    m[3][4] = Color.BLACK
    m[3][5] = Color.BLACK
    m[3][6] = Color.BLACK
    m[3][8] = Color.BLACK

    m[4][0] = Color.BLACK
    m[4][2] = Color.BLACK
    m[4][7] = Color.BLACK

    m[5][0] = Color.BLACK
    m[5][2] = Color.BLACK
    m[5][5] = Color.BLACK
    m[5][7] = Color.BLACK
    m[5][8] = Color.BLACK
    m[5][9] = Color.BLACK

    m[6][4] = Color.BLACK
    m[6][6] = Color.BLACK
    m[6][9] = Color.BLACK

    m[7][0] = Color.BLACK
    m[7][2] = Color.BLACK
    m[7][4] = Color.BLACK
    m[7][6] = Color.BLACK

    m[8][0] = Color.BLACK
    m[8][2] = Color.BLACK
    m[8][3] = Color.BLACK
    m[8][7] = Color.BLACK
    m[8][8] = Color.BLACK
    m[8][9] = Color.BLACK

    m[9][7] = Color.BLACK
    m[9][8] = Color.BLACK

    print(matrix_to_string(m))

    flip_color(m, 5, 4)

    print(matrix_to_string(m))

    flip_color(m, 3, 6)

    print(matrix_to_string(m))

    print("Main done...")


if __name__ == "__main__":
    main()