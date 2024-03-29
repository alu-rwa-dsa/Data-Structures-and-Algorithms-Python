import unittest  # import the unittest module to test the class methods

from implementation_9.is_heap import isMinHeap


class TestIsHeap(unittest.TestCase):
    def test1(self):
        arr = [1, 5, 6, 10, 12, 13, 14, 12, 15, 20]
        self.assertEqual(isMinHeap(arr), True)

    def test2(self):
        arr = []
        self.assertEqual(isMinHeap(arr), False)

    def test3(self):
        arr = [1, 2, 5, 0, 6, 7, 8]
        self.assertEqual(isMinHeap(arr), False)

    def test4(self):
        arr = [1, 2, 5, 3, 6, 7, 8, 1]
        self.assertEqual(isMinHeap(arr), False)

    def test5(self):
        arr = [1]
        self.assertEqual(isMinHeap(arr), True)


if __name__ == '__main__':
    unittest.main()
