import unittest
import main

class Test_TestEncode(unittest.TestCase):
    def test_encode_z_1(self):
        self.assertEquals(main.encode('z', 1), 'a')

    def test_encode_a_1(self):
        self.assertEquals(main.encode('a', 1), 'b')

    def test_encode_a_25(self):
        self.assertEquals(main.encode('a', 25), 'z')

    def test_encode_z_25(self):
        self.assertEquals(main.encode('z', 25), 'y')

    def test_encode_AbCdEfG_1(self):
        self.assertEquals(main.encode('AbCdEfG', 1), 'AcCeEgG')

    def test_encode_AbCdEfG_25(self):
        self.assertEquals(main.encode('AbCdEfG', 25), 'AaCcEeG')

class Test_TestDecode(unittest.TestCase):
    def test_decode_z_1(self):
        self.assertEquals(main.decode('z', 1), 'y')

    def test_decode_a_1(self):
        self.assertEquals(main.decode('a', 1), 'z')

    def test_decode_a_25(self):
        self.assertEquals(main.decode('a', 25), 'b')

    def test_decode_z_25(self):
        self.assertEquals(main.decode('z', 25), 'a')

    def test_decode_AbCdEfG_1(self):
        self.assertEquals(main.decode('AbCdEfG', 1), 'AaCcEeG')

    def test_decode_AbCdEfG_25(self):
        self.assertEquals(main.decode('AbCdEfG', 25), 'AcCeEgG')

if __name__ == '__main__':
    unittest.main()