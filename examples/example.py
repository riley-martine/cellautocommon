#!/usr/bin/env python3
"""Example usage of package."""

from functions import get_next_row, get_rows

if __name__ == "__main__":
    FIRST_ROW = '101'  # Can be ints or strings
    RULE = 30      # Rule number 0-255

    print("First Row: " + str(FIRST_ROW))
    print("Rule number: " + str(RULE))


    SECOND_ROW = get_next_row(row=FIRST_ROW, rule=RULE)
    print("Second Row: " + str(SECOND_ROW))

    FIRST_FIVE_ROWS = get_rows(
        first_row=FIRST_ROW, rule=RULE, number_of_rows=5)
    print("First five rows: " + str(FIRST_FIVE_ROWS))

    FIRST_FIVE_ROWS_PADDED = get_rows(
        first_row=FIRST_ROW, rule=RULE, number_of_rows=5, pad_rows=True)
    print("First five rows(padded): " + str(FIRST_FIVE_ROWS_PADDED))

    print("First five rows(padded) as a triangle: ")
    for row in FIRST_FIVE_ROWS_PADDED:
        print(row)
