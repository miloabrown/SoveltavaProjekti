import unittest
import nopee
import hidas

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

    def testaa_quick_sort(self):
        lista2 = [2, 4, 0, 1, 3]
        nopee.quick_sort(lista2)
        lista21 = np.arange(5)
        self.assertTrue(lista2, lista21)
    
    def testaa_bubble_sort(self):
        lista3 = [3, 0, 1, 2, 4]
        hidas.bubble_sort(lista3)
        lista31 = np.arange(5)
        self.assertTrue(lista3, lista31)




if __name__ == "__main__":
    unittest.main()