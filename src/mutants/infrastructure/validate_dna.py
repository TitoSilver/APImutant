from typing import List

def has_number(dna: List[str]) -> bool:
    '''
        Validates the existence of numbers in the Array 
    '''
    is_number = False
    for row in dna:
        number_in_row = any(char.isdigit() for char in row)
        if number_in_row:
            return True
    return is_number
