from unittest import TestCase
from main import get


class Test(TestCase):

    def test_get(self):
        self.assertEqual(get([2, 4, 6, 7, 8, 10]), 7)
        self.assertEqual(get([1, 2, 3, 5, 7, 9]), 2)
