import spam_10 as spam
import cube
import pytest
import unittest


class TestCube(unittest.TestCase):

    def test_0(self):
        self.assertEqual(cube.cube(0), 0)

    def test_1(self):
        self.assertEqual(cube.cube(1), 1)

    def test_2(self):
        self.assertEqual(cube.cube(2), 8)

    def test_3(self):
        self.assertEqual(cube.cube(3), 27)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            cube.cube()

    def test_exception_str(self):
        with self.assertRaises(TypeError):
            cube.cube('x')


class TestPyCube(object):

    def test_0(self):
        assert cube.cube(0) == 0

    def test_1(self):
        assert cube.cube(1) == 1

    def test_2(self):
        assert cube.cube(2) == 8

    def test_3(self):
        assert cube.cube(3) == 27

    def test_no_arguments(self):
        with pytest.raises(TypeError):
            cube.cube()

    def test_exception_str(self):
        with pytest.raises(TypeError):
            cube.cube('x')

##############################################################################


def test_spam_equal_correct():
    a = spam.Spam(5)
    b = spam.Spam(5)

    assert a == b


def test_spam_equal_broken():
    a = spam.Spam(5)
    b = spam.Spam(10)

    assert a != b
