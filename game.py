import numpy as np
import random


def draw_field(field):
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            print(field[i][j], '| ', end='')
        print()
        print("----------------------------------------")


def check_cell(field, i, j):
    if field[i][j] == 'O' or field[i][j] == 'X':
        return False
    else:
        return True


def step_human(field, i, j):
    field[i][j] = "X"
    draw_field(field)


def step_computer(field):
    result = False
    counter = 1
    while not result and counter <= 50:
        i = random.randint(0, (field.shape[0] - 1))
        j = random.randint(0, (field.shape[1] - 1))
        if check_cell(field, i, j):
            if i == 0:
                if j == 0:
                    if field[i+1][j] != 'O' and field[i][j+1] != 'O' and field[i+1][j+1] != 'O':
                        field[i][j] = 'O'
                        result = True
                        break
                elif j == (field.shape[1] - 1):
                    if field[i+1][j] != 'O' and field[i][j-1] != 'O' and field[i+1][j-1] != 'O':
                        field[i][j] = 'O'
                        result = True
                        break
                else:
                    if field[i][j-1] != 'O' and field[i][j+1] != 'O' and\
                            field[i+1][j] != 'O' and field[i+1][j-1] != 'O' and field[i+1][j+1] != 'O':
                        field[i][j] = 'O'
                        result = True
                        break
            elif i == (field.shape[0] - 1):
                if j == (field.shape[1] - 1):
                    if field[i][j-1] != 'O' and field[i-1][j-1] != 'O' and field[i-1][j] != 'O':
                        field[i][j] = 'O'
                        result = True
                        break
                elif j == 0:
                    if field[i-1][j] != 'O' and field[i-1][j+1] != 'O' and field[i][j+1] != 'O':
                        field[i][j] = 'O'
                        result = True
                        break
                else:
                    if field[i][j-1] != 'O' and field[i][j+1] != 'O' and \
                            field[i-1][j-1] != 'O' and field[i-1][j] != 'O' and field[i-1][j+1] != 'O':
                        field[i][j] = 'O'
                        result = True
                        break
            elif j == 0:
                if field[i-1][j] != 'O' and field[i-1][j+1] != 'O' and field[i][j+1] != 'O':
                    field[i][j] = 'O'
                    result = True
                    break
            elif j == (field.shape[1] - 1):
                if field[i-1][j] != 'O' and field[i-1][j-1] != 'O' and field[i][j-1] != 'O':
                    field[i][j] = 'O'
                    result = True
                    break
            else:
                if field[i-1][j-1] != 'O' and field[i-1][j] != 'O' and field[i-1][j+1] != 'O' and field[i][j-1] != 'O' and \
                        field[i][j+1] != 'O' and field[i+1][j-1] != 'O' and field[i+1][j] != 'O' and field[i+1][j+1] != 'O':
                    field[i][j] = 'O'
                    result = True
                    break
        counter += 1
    if not result:
        while not result:
            i = random.randint(0, (field.shape[0] - 1))
            j = random.randint(0, (field.shape[1] - 1))
            if check_cell(field, i, j):
                field[i][j] = 'O'
                result = True
                break
    return i, j


def check_loss_row(field, i, j):
    result_1 = 1
    tmp_left = j - 1
    while result_1 != 5 and tmp_left >= 0:
        if field[i][j] == field[i][tmp_left]:
            result_1 += 1
            tmp_left -= 1
        else:
            break
    tmp_right = j + 1
    result_2 = 1
    while result_2 != 5 and tmp_right <= (field.shape[1] - 1):
        if field[i][j] == field[i][tmp_left]:
            result_2 += 1
            tmp_left += 1
        else:
            break
    result = max(result_1, result_2)
    if result >= 5:
        return True
    else:
        return False


def check_loss_column(field, i, j):
    result_1 = 1
    tmp_up = i - 1
    while result_1 != 5 and tmp_up >= 0:
        if field[i][j] == field[tmp_up][j]:
            result_1 += 1
            tmp_up -= 1
        else:
            break
    tmp_down = i + 1
    result_2 = 1
    while result_2 != 5 and tmp_down <= (field.shape[0] - 1):
        if field[i][j] == field[tmp_down][j]:
            result_2 += 1
            tmp_down += 1
        else:
            break
    result = max(result_1, result_2)
    if result >= 5:
        return True
    else:
        return False


def check_loss_main_diagonal(field, i, j):
    result_1 = 1
    i_up = i - 1
    j_up = j - 1
    while result_1 != 5 and i_up >= 0 and j_up >= 0:
        if field[i][j] == field[i_up][j_up]:
            result_1 += 1
            i_up -= 1
            j_up -= 1
        else:
            break
    i_down = i + 1
    j_down = i + 1
    result_2 = 1
    while result_2 != 5 and i_down <= (field.shape[0]-1) and j_down <= (field.shape[1]-1):
        if field[i][j] == field[i_down][j_down]:
            result_2 += 1
            i_down += 1
            j_down += 1
        else:
            break
    result = max(result_1, result_2)
    if result >= 5:
        return True
    else:
        return False


def check_loss_side_diagonal(field, i, j):
    result_1 = 1
    i_up = i - 1
    j_up = j + 1
    while result_1 != 5 and i_up >= 0 and j_up <= (field.shape[1] - 1):
        if field[i][j] == field[i_up][j_up]:
            result_1 += 1
            i_up -= 1
            j_up += 1
        else:
            break
    i_down = i + 1
    j_down = j - 1
    result_2 = 1
    while result_2 != 5 and i_down <= (field.shape[0] - 1) and j_down >= 0:
        if field[i][j] == field[i_down][j_down]:
            result_2 += 1
            i_down += 1
            j_down -= 1
        else:
            break
    result = max(result_1, result_2)
    if result >= 5:
        return True
    else:
        return False


def check_loss(field, i, j):
    return check_loss_row(field, i, j) + check_loss_column(field, i, j) + \
           check_loss_main_diagonal(field, i, j) + check_loss_side_diagonal(field, i, j)


if __name__ == "__main__":
    game_field = np.empty(shape=(10, 10), dtype=str)
    game_field[:] = '.'
    loss = False
    counter = 0
    draw_field(game_field)
    while not loss:
        print('Ваш ход')
        check = False
        while not check:
            row = int(input('Введите номер строки '))
            col = int(input('Введите номер столбца '))
            if check_cell(game_field, row, col):
                check = True
                step_human(game_field, row, col)
                counter += 1
            else:
                print('Ячейка уже занята. Попробуйте другую')
        if check_loss(game_field, row, col):
            loss = True
            print('К сожалению вы проиграли :(')
            break
        else:
            print()
            print('Ход компьютера')
            print()
            step = step_computer(game_field)
            draw_field(game_field)
            counter += 1
            comp_row = step[0]
            comp_col = step[1]
            if check_loss(game_field, comp_row, comp_col):
                loss = True
                print('Компьютер проиграл! Поздравляю, Вы выиграли!')
                break
        if counter == 100:
            print('Ничья!')
            break
