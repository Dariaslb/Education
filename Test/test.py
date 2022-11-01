import unittest
from Str.main import String

class TestString(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.obj_1 = String("11")
        self.obj_2 = String("ghthtr")
        print(self.obj_1.string)
        print(self.obj_2.string)

    def test_type(self):
        with self.assertRaises(TypeError):
            self.obj_3 = String(4)
            print("Typeerror")

    def test__cal__(self):
        self.assertEqual(self.obj_1("None"), "None")
        self.assertEqual(self.obj_2("dedede"), "dedede")

    def test__add__(self):
        self.assertEqual(self.obj_1 + self.obj_2, "11ghthtr")

if __name__ == '__main__':
    unittest.main()
