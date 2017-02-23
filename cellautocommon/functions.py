#!/usr/bin/env python3
"""Functions for working with cellular automata."""
from typing import List
from rules import RuleList


def get_next_row(row: str, rule: int=None, rule_dict: RuleList=None) -> str:
    """Get next row of a 1D automaton.

    Keyword arguments:
    row -- string composed of 1s and 0s
    rule -- rule between 0 and 255, inclusive
    """

    # Allow passing of rule dictionary to save memory when computing many rows
    if rule:
        rule_dict = RuleList(rule).rules
    if not rule_dict:
        raise Exception("No rules passed!")

    # If scanning the edge, we need two more cells to scan every group of 3
    scan_row = '00' + row + '00'

    next_row = ''
    next_row_length = len(row) + 2

    for pos in range(next_row_length):
        local_three = scan_row[pos:pos + 3]
        next_row += (rule_dict[local_three.ljust(3, '0')])
    return next_row


def get_rows(first_row: str, rule: int, number_of_rows: int, pad_rows: bool=False) -> List:
    """Get rows [0, number_of_rows] of a 1D automaton.

    Keyword arguments:
    first_row -- string composed of 1s and 0s
    rule -- rule between 0 and 255, inclusive
    number_of_rows -- number of rows to get
    pad_rows -- whether to pad list with zeros, making all elements the same length

    Returns list of length $number_of_rows as strings
    """

    # So we don't have to create a new object each time
    rule_dict = RuleList(rule).rules

    # Initialize list
    rows = [first_row]

    # (number_of_rows - 1) is so get_rows(..., 5) returns five rows
    for _ in range(number_of_rows - 1):
        rows.append(get_next_row(row=rows[-1], rule_dict=rule_dict))

    if pad_rows:
        longest_row_length = len(rows[-1])
        rows = list('{row:0^{max_length}}'.format(
            row=row, max_length=longest_row_length) for row in rows)

    return rows
