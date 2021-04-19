import unittest
import algorithmAnalysis as aA
import sortingAlgo as sA
import searchAlgo as seA
import numpy as np

#yksikkötestiluokka

class testLists(unittest.TestCase):
    def testList(self):
        """
        Testi, että listassa on ylipäätään mitään
        """
        lista = aA.getSorted()
        self.assertEqual(len(lista), 10000000)
    def testList2(self):
        """
        Testi, että listassa on ylipäätään mitään
        """
        lista = aA.getUnsorted()
        self.assertEqual(len(lista), 100000)
    
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

    def testaa_quick_sort(self):
        lista2 = [2, 4, 0, 1, 3]
        sA.algoritmi1(lista2)
        lista21 = np.arange(5)
        self.assertTrue(lista2, lista21)
    
    def testaa_bubble_sort(self):
        lista3 = [3, 0, 1, 2, 4]
        sA.algoritmi2(lista3)
        lista31 = np.arange(5)
        self.assertTrue(lista3, lista31)
    


if __name__ == "__main__":
    unittest.main()