import unittest

def is_palindrome(palindrome_con_espacio):
    
    palindrome_sin_espacio= ""
    for i in range(0, len(palindrome_con_espacio)):
        if palindrome_con_espacio[i] != " ":
            palindrome_sin_espacio += palindrome_con_espacio[i].lower()
    
    for indice in range(0, len(palindrome_sin_espacio)):
        
        if palindrome_sin_espacio[indice] != palindrome_sin_espacio[-(indice+1)]:
            
            return False
    return True
            
        
class TestPalindrome (unittest.TestCase):
    def test_A (self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)
    def test_aa (self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)
    def test_ab (self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado, False)
    def test_aba (self):
        resultado = is_palindrome('aba')
        self.assertEqual(resultado, True)
    def test_acb (self):
        resultado = is_palindrome('acb')
        self.assertEqual(resultado, False)
    def test_abba (self):
        resultado = is_palindrome('abba')
        self.assertEqual(resultado, True)
    def test_abca (self):
        resultado = is_palindrome('abca')
        self.assertEqual(resultado, False)
    def test_abbc (self):
        resultado = is_palindrome('abbc')
        self.assertEqual(resultado, False)
    def test_acbbca (self):
        resultado = is_palindrome('acbbca')
        self.assertEqual(resultado, True)
    def test_acbsc (self):
        resultado = is_palindrome('acbsc')
        self.assertEqual(resultado, False)
    def test_neuquen (self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)
    def test_neuqen (self):
        resultado = is_palindrome('neuqen')
        self.assertEqual(resultado, False)
    def test_Neunem (self):
        resultado = is_palindrome('Neunem')
        self.assertEqual(resultado, False)
    def test_ELPEP (self):
        resultado = is_palindrome('ELPEP')
        self.assertEqual(resultado, False)
    def test_ac_a (self):
        resultado = is_palindrome('ac a')
        self.assertEqual(resultado, True )
    def test_Neu_quen (self):
        resultado = is_palindrome('Neu quen')
        self.assertEqual(resultado, True)
    def test_NE_en (self):
        resultado = is_palindrome('NE en')
        self.assertEqual(resultado, True)


if __name__ == "__main__":
    unittest.main()


