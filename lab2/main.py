import vector_module
import to_json_module
import unittest


class JsonTest(unittest.TestCase):
    def test_is_str(self):
        self.assertTrue(to_json_module.obj_to_json([5, 5, 6]).__class__, str)

    def test_not_support(self):
        self.assertIsNone(to_json_module.obj_to_json((5, 5)))


class VectorTest(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(vector_module.Vector([5, 5]) + vector_module.Vector([5, 5]), vector_module.Vector([10, 10]))

    def test_can_not_plus(self):
        self.assertIsNone(vector_module.Vector([5, 5]) + vector_module.Vector([5, 5, 5]))

    def test_plus_not_vector(self):
        with self.assertRaises(AttributeError):
            print(vector_module.Vector([5, 5]) + 5)


def task_3():
    vector1 = vector_module.Vector([5, 5])
    vector2 = vector_module.Vector([5, 5])
    print(vector1)
    print(vector2 + vector1)
    print(vector2 - vector1)
    print(vector2 * vector1)
    print(vector1.mul_number(5))
    print(vector1 == vector2)
    print(vector1.get_length())
    print(vector1[0])


def task_2():
    dictionary = {"1": 1, "2": "word", "3":  False, "4": [123, 456], "5":{"4.1": 1, "4.2": "2"}}
    print(dictionary)
    print(to_json_module.obj_to_json(dictionary))


task_2()
task_3()
