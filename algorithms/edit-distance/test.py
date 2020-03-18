import unittest

from edit_distance import edit_distance as dist 


class TestEditDistance(unittest.TestCase):
    

    def test_empty(self):
        self.assertEqual(0, dist('', ''))


    def test_single_match(self):
        self.assertEqual(0, dist('a', 'a'))


    def test_single_insert(self):
        self.assertEqual(1, dist('hkie', 'hokie'))


    def test_single_replace(self):
        self.assertEqual(1, dist('hokia', 'hokie'))


    def test_single_delete(self):
        self.assertEqual(1, dist('hokies', 'hokie'))


    def test_multiple_one(self):
        self.assertEqual(5, dist('01234', '56789'))


    def test_multiple_two(self):
        self.assertEqual(4, dist('abcccde', 'fgccchi'))


if __name__ == '__main__':
    unittest.main()
