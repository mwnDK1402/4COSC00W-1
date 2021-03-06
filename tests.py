import unittest
import shiftcipher

class Test_TestEncode(unittest.TestCase):
    def test_encode_z_1(self):
        self.assertEqual(shiftcipher.encode('z', 1), 'a')

    def test_encode_a_1(self):
        self.assertEqual(shiftcipher.encode('a', 1), 'b')

    def test_encode_a_25(self):
        self.assertEqual(shiftcipher.encode('a', 25), 'z')

    def test_encode_z_25(self):
        self.assertEqual(shiftcipher.encode('z', 25), 'y')

    def test_encode_AbCdEfG_1(self):
        self.assertEqual(shiftcipher.encode('AbCdEfG', 1), 'AcCeEgG')

    def test_encode_AbCdEfG_25(self):
        self.assertEqual(shiftcipher.encode('AbCdEfG', 25), 'AaCcEeG')

    def test_encode_æøå_1(self):
        self.assertEqual(shiftcipher.encode('æøå', 1), 'æøå')

class Test_TestDecode(unittest.TestCase):
    def test_decode_z_1(self):
        self.assertEqual(shiftcipher.decode('z', 1), 'y')

    def test_decode_a_1(self):
        self.assertEqual(shiftcipher.decode('a', 1), 'z')

    def test_decode_a_25(self):
        self.assertEqual(shiftcipher.decode('a', 25), 'b')

    def test_decode_z_25(self):
        self.assertEqual(shiftcipher.decode('z', 25), 'a')

    def test_decode_AbCdEfG_1(self):
        self.assertEqual(shiftcipher.decode('AbCdEfG', 1), 'AaCcEeG')

    def test_decode_AbCdEfG_25(self):
        self.assertEqual(shiftcipher.decode('AbCdEfG', 25), 'AcCeEgG')

    def test_dont_decode_æøå_1(self):
        self.assertEqual(shiftcipher.decode('æøå', 1), 'æøå')

class Test_TestFindRotations(unittest.TestCase):
    def test_khoor_zruog_wo(self):
        self.assertEqual(shiftcipher.find_possible_rotations('khoor zruog', 'wo'), [3, 18])

if __name__ == '__main__':
    unittest.main()