import unittest

import algorithmAnalysis as aA
import sortingAlgo as sA
import searchAlgo as seA



class testLists(unittest.TestCase):
    def testList(self):
        """
        Testi, että listoissa on ylipäätään mitään
        """
        lista1 = aA.getSorted()
        self.assertEqual(len(lista1), 100000)




if __name__ == "__main__":
    unittest.main()