import numpy as np
from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse, Response

class Mutant():
    dna: dict
    status: bool

    def __init__(self,dna) -> None:
        self.dna = dna

    def has_mutant(self) -> bool:
        if not self.dna:
            self.status = False
            return False
        count_mutations = 0
        chars_in_row = len(self.dna["dna"][0])
        unique_string = ''.join(row for row in self.dna["dna"])
        horizontal_status = self.horizontal_check(unique_string, chars_in_row)
        count_mutations += horizontal_status
        if count_mutations >= 2:
            self.status = True
            return True
        vertical_status = self.vertical_check(unique_string, chars_in_row)
        count_mutations += vertical_status
        if count_mutations >= 2:
            self.status = True
            return True
        diagonal_status = self.diagonal_check(self.dna["dna"])
        count_mutations += diagonal_status
        if count_mutations >= 2:
            self.status = True
            return True
        self.status = False
        return False

    def horizontal_check(self, unique_string: str, chars_in_row: int) -> int:
        horizontal_mutations = 0
        for idx in range(0, chars_in_row):
            first_idx = idx * chars_in_row
            final_idx = (idx+1) * chars_in_row
            sub_string = unique_string[first_idx:final_idx]
            count_mutations = self.check_mutation(sub_string)
            if count_mutations:
                horizontal_mutations += count_mutations
        return horizontal_mutations
    
    def vertical_check(self,unique_string: str, chars_in_row: int) -> int:
        vertical_mutations = 0
        for idx in range(0, chars_in_row):
            sub_string = unique_string[idx::chars_in_row]
            count_mutations = self.check_mutation(sub_string)
            if count_mutations:
                vertical_mutations += count_mutations
        return vertical_mutations

    def diagonal_check(self,dna: List[str]) -> int:
        matrix = np.array([[char_ for char_ in row] for row in dna])
        diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
        diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))
        list_all_diags = [''.join(char_) for char_ in diags]
        list_sub_string = [sub_string for sub_string in list_all_diags if len(sub_string) > 3]
        diagonal_mutations = 0
        for sub_string in list_sub_string:
            count_mutations = self.check_mutation(sub_string)
            if count_mutations:
                diagonal_mutations += count_mutations
        return diagonal_mutations

    def check_mutation(self, sub_string: str) -> int:
        '''
        Se utilizo Rabin-Karp string matching
        '''
        count_mutations = 0
        set_hashes = set(hash(char_*4) for char_ in ('A','T','C','G'))
        for idx in range(0,len(sub_string)-4):
            is_mutant = hash(sub_string[idx:idx+4]) in set_hashes
            if is_mutant:
                count_mutations += 1
        return count_mutations
