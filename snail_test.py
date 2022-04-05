from random import random
import unittest
from unittest.mock import patch
import snail


class SnailTest(unittest.TestCase):

    def testGetSnailMatrixNeg(self):
        self.assertRaises(Exception, snail.get_snail_matrix, -1)

    def testGetSnailMatrixRank0(self):
        self.assertEqual(snail.get_snail_matrix(0), [])

    def testGetSnailMatrixRank1(self):    
        self.assertEqual(snail.get_snail_matrix(1), [[0]])

    def testGetSnailMatrixRank2(self):        
        self.assertEqual(snail.get_snail_matrix(2), [[0, 1], [3, 2]])

    def testGetSnailMatrixRank3(self):        
        self.assertEqual(
            snail.get_snail_matrix(3),
            [[0, 1, 2],
             [7, 8, 3],
             [6, 5, 4]]
        )

    def testGetSnailMatrixRank4(self):        
        self.assertEqual(
            snail.get_snail_matrix(4),
            [[0,  1,  2,  3],
             [11, 12, 13, 4],
             [10, 15, 14, 5],
             [9,  8,  7,  6]])

    @patch('snail.get_snail_matrix')
    def testGetSnailZeroes0(self, get_snail_matrix):
        get_snail_matrix.return_value = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(
            snail.get_snail(1),
            '1 1 1\n1 1 1\n1 1 1'
        )

    @patch('snail.get_snail_matrix')
    def testGetSnailZeroes1(self, get_snail_matrix):
        get_snail_matrix.return_value = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(
            snail.get_snail(5),
            '01 01 01\n01 01 01\n01 01 01'
        )

    @patch('snail.get_snail_matrix')
    def testGetSnailZeroes2(self, get_snail_matrix):
        get_snail_matrix.return_value = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(
            snail.get_snail(11),
            '001 001 001\n001 001 001\n001 001 001'
        )

if __name__ == '__main__':
    unittest.main()
