import unittest
from src.mutants.domain.mutant import Mutant

DNA_MUTANT = {
        "dna":[
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"
        ]
    }

DNA_HUMAN = {
    "dna":[
        "ATGCGA",
        "CAGTGC",
        "TTATTT",
        "AGACGG",
        "GCGTCA",
        "TCACTG"
    ]
}

class TestMutants(unittest.TestCase):
    def test_is_mutant_true(self) -> bool:
        #GIVEN
        mutant = Mutant(DNA_MUTANT)
        #THEN
        self.assertTrue(mutant.is_mutant)

    def test_is_not_mutant(self) -> bool:
        #GIVEN
        mutant = Mutant(DNA_HUMAN)
        #THEN
        self.assertFalse(mutant.is_mutant)

    def test_mutant_horizontal_check_true(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_MUTANT)
        chars_in_row = len(DNA_MUTANT['dna'][0])
        #THEN
        self.assertEqual(mutant.horizontal_check(chars_in_row), 1)

    def test_mutant_horizontal_check_false(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_MUTANT)
        chars_in_row = len(DNA_MUTANT['dna'][0])
        #THEN
        self.assertFalse(mutant.horizontal_check(chars_in_row) != 1)

    def test_human_horizontal_check_true(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_HUMAN)
        chars_in_row = len(DNA_HUMAN['dna'][0])
        #THEN
        self.assertEqual(mutant.horizontal_check(chars_in_row), 0)

    def test_human_horizontal_check_false(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_HUMAN)
        chars_in_row = len(DNA_HUMAN['dna'][0])
        #THEN
        self.assertFalse(mutant.horizontal_check(chars_in_row) != 0)

    def test_mutant_vertical_check_true(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_MUTANT)
        chars_in_row = len(DNA_MUTANT['dna'][0])
        #THEN
        self.assertEqual(mutant.vertical_check(chars_in_row), 1)

    def test_mutant_vertical_check_false(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_MUTANT)
        chars_in_row = len(DNA_MUTANT['dna'][0])
        #THEN
        self.assertFalse(mutant.vertical_check(chars_in_row) != 1)

    def test_human_vertical_check_true(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_HUMAN)
        chars_in_row = len(DNA_HUMAN['dna'][0])
        #THEN
        self.assertEqual(mutant.vertical_check(chars_in_row), 0)

    def test_human_vertical_check_false(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_HUMAN)
        chars_in_row = len(DNA_HUMAN['dna'][0])
        #THEN
        self.assertFalse(mutant.vertical_check(chars_in_row) != 0)

    def test_mutant_diagonal_check_true(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_MUTANT)
        #THEN
        self.assertEqual(mutant.diagonal_check(mutant.dna), 1)

    def test_mutant_diagonal_check_false(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_MUTANT)
        #THEN
        self.assertFalse(mutant.diagonal_check(mutant.dna) != 1)

    def test_human_diagonal_check_true(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_HUMAN)
        #THEN
        self.assertEqual(mutant.diagonal_check(mutant.dna), 0)

    def test_human_diagonal_check_false(self) -> int:
        #GIVEN
        mutant = Mutant(DNA_HUMAN)
        #THEN
        self.assertFalse(mutant.diagonal_check(mutant.dna) != 0)
