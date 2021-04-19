import unittest

import algorithmAnalysis as aA
import sortingAlgo as sA
import searchAlgo as seA
import numpy as np



class testLists(unittest.TestCase):
    def testList(self):
        """
        Testi, että listoissa on ylipäätään mitään
        """
        lista1 = aA.getSorted()
        self.assertEqual(len(lista1), 100000)

    def testLinearSearch(self):
        """
        Testataan Lineaarihaku algoritmin toimivuus
        """
        lista1 = np.arange(5)
        self.assertTrue(seA.algoritmi1(lista1,4),4)
    
    def testBinarySearch(self):
        """
        Testataan Binäärihaku algoritmin toimivuus
        """
        lista1 = np.arange(5)
        self.assertTrue(seA.algoritmi2(lista1,4),4)

if __name__ == "__main__":
    unittest.main()