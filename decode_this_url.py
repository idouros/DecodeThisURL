# Copyright (c) 2025 Yannis Douros
# Please read the LICENSE file

import pandas as pd

def get_max_in_column(col, char_table):
    max_val = -1
    num_rows = char_table.shape[0]
    for i in range(1, num_rows):
        val = int(char_table[col][i])
        if val > max_val:
            max_val = val
    return max_val

def decode_this_url(input_url):
    char_table = pd.read_html(input_url, encoding='utf-8')[0]
    max_x_coord = get_max_in_column(0, char_table)
    max_y_coord = get_max_in_column(2, char_table)
    num_rows = char_table.shape[0]

    result = []
    for i in range(1, max_y_coord+2):
        result.append([' '] * (max_x_coord+1))

    for i in range(1, num_rows):
        x = int(char_table[0][i])
        y = int(char_table[2][i])
        c = char_table[1][i]
        result[y][x] = c
    return result

def print_result(result):
    for i in range(0, len(result)):
        print("".join(result[i]))

def main():
    url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    result = decode_this_url(url)
    print_result(result)

if __name__ == "__main__":
    main()
