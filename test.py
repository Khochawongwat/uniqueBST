import unittest

from main import generateBTS

class TestGenerateBTS(unittest.TestCase):
    
    def test_generateBTS_3(self):
        self.assertEqual(generateBTS(3), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [3, 2, 1]])

    def test_generateBTS_1(self):
        self.assertEqual(generateBTS(1), [[1]])

    def test_generateBTS_0(self):
        self.assertEqual(generateBTS(0), [[]])

    def test_generateBTS_2(self):
        self.assertEqual(generateBTS(2), [[1, 2], [2, 1]])

    def test_dupes(self):
        for i in range(1, 12):
            trees = generateBTS(i)
            self.assertEqual(sorted(trees), sorted([list(x) for x in set(tuple(tree) for tree in trees)]))
if __name__ == '__main__':
    unittest.main()