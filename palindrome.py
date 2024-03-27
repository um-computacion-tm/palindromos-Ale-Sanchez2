import unittest

def is_palindrome(palindrome_con_espacio):
    
    palindrome_sin_espacio= ""
    for i in range(0, len(palindrome_con_espacio)):
        if palindrome_con_espacio[i] != " ":
            palindrome_sin_espacio += palindrome_con_espacio[i]
    
    for indice in range(0, len(palindrome_sin_espacio)):
        
        if palindrome_sin_espacio[indice] != palindrome_sin_espacio[-(indice+1)]:
            
            return False
    return True
            
        


class TestPalindrome (unittest.TestCase):
    def test_A (self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)
    def test_C (self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)
    def test_B (self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)
    def test_Q (self):
        resultado = is_palindrome('ELPEP')
        self.assertEqual(resultado, False)
    def test_X (self):
        resultado = is_palindrome('ac a')
        self.assertEqual(resultado, True )

unittest.main()

