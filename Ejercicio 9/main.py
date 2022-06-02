import unittest
from Palindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    __palindromo = None

    def setUp(self):
        self.__palindromo = Palindromo("MENEM")
    
    def testPalindromo(self):
        self.assertEqual(self.__palindromo.esPalindromo(), True)

    def testNoPalindromo(self):
        self.__palindromo.setPalabra("ANDREA")
        self.assertEqual(self.__palindromo.esPalindromo(), False)

    def testSinPalabra(self):
        self.__palindromo.setPalabra("")
        self.assertEqual(self.__palindromo.esPalindromo(), False)
        
if __name__ == "__main__":
    unittest.main()