#!/usr/bin/python3
""" Unittest for Base class. """
import unittest
from models.base import Base



class TestBase(unittest.TestCase):
    """ Test Base class. """

    @classmethod
    def setUpClass(cls):
        """ Setup Base. """
        cls.base_instance = Base()

    def test_private(self):
        """ Test nb_objects is private. """
        self.assertTrue(hasattr(self.base_instance, "_Base__nb_objects"))

    def test_initialization(self):
        """ Test Base initalizes at zero. """
        self.assertEqual(getattr(self.base_instance, "_Base__nb_objects"), 0)

    def test_startUp(self):
        """ Test Base is <class> with id '1'. """
        self.assertEqual(str(type(self.base_instance)),
                         "<class 'models.base.Base'>")
        self.assertEqual(self.base_instance.__dict__, {"id": 1})
        self.assertEqual(self.base_instance.id, 1)

    def test_constructive_ids(self):
        """ Test id's are constructive. """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_custom_id_int(self):
        """ Test id with an integer. """
        i = 42
        base = Base(i)
        self.assertEqual(base.id, i)

    def test_custom_id_str(self):
        """ Test id with a string. """
        i = "Blythe"
        base = Base(i)
        self.assertEqual(base.id, i)

    def test_custom_id_keyword(self):
        """ Test id with the 'id' keyword. """
        i = 42
        base = Base(id=i)
        self.assertEqual(base.id, i)

    def test_to_json_string(self):
        """ Test to_json_string() method. """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        diction = [{'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5}]
        self.assertEqual(Base.to_json_string(diction), str(diction))
        diction = [{"Blythe": 42}]
        self.assertEqual(Base.to_json_string(diction), '[{"Blythe": 42}]')
        diction = [{"Blythe": 42}, {"Lockhart": 25}]
        self.assertEqual(Base.to_json_string(d), '[{"Blythe": 42}, \
                                                   {"Lockhart": 25}]')

    def test_save_to_file_rectangle(self):
        """ Test save_to_file() method for rectangles. """
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as i:
            self.assertEqual(len(i.read()), 42)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as i:
            self.assertEqual(i.read(), "[]")
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        rect2 = Rectangle(1, 2)
        Rectangle.save_to_file([rect2])
        with open("Rectangle.json", "r") as i:
            self.assertEqual(len(i.read()), 42)

    def test_save_to_file_square(self):
        """ Test save_to_file() method for squares. """
        square1 = Square(1)
        square2 = Square(1, 2, 3)
        Square.save_to_file([s1, square2])
        with open("Square.json", "r") as i:
            self.assertEqual(len(i.read()), 42)
        Square.save_to_file(None)
        with open("Square.json", "r") as i:
            self.assertEqual(i.read(), "[]")
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        square2 = Square(1)
        Square.save_to_file([square2])
        with open("Square.json", "r") as i:
            self.assertEqual(len(i.read()), 42)

    def test_create(self):
        """ Test create() method. """
        rect1 = Rectangle(1, 2, 3)
        diction = rect1.to_dictionary()
        rect2 = Rectangle.create(**diction)
        self.assertEqual(str(rect1), str(rect2))
        self.assertFalse(rect1 is rect2)
        self.assertFalse(rect1 == rect2)

    def test_load_from_file_rectangle(self):
        """ Test load_from_file() method for rectangles. """
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2)
        rects_in = [rect1, rect2]
        Rectangle.save_to_file(rects_in)
        rects_out = Rectangle.load_from_file()
        self.assertNotEqual(id(rects_in[0]), id(rects_out[0]))
        self.assertEqual(str(rects_in[0]), str(rects_out[0]))
        self.assertNotEqual(id(rects_in[1]), id(rects_out[1]))
        self.assertEqual(str(rects_in[1]), str(rects_out[1]))

    def test_load_from_file_square(self):
        """Test load_from_file() method for squares. """
        square1 = Square(1)
        square2 = Square(1, 2, 3)
        squares_in = [s1, s2]
        Square.save_to_file(squares)
        squares_out = Square.load_from_file()
        self.assertNotEqual(id(squares_in[0]), id(squares_out[0]))
        self.assertEqual(str(squares_in[0]), str(squares_out[0]))
        self.assertNotEqual(id(squares_in[1]), id(squares_out[1]))
        self.assertEqual(str(squares_in[1]), str(squares_out[1]))


if __name__ == "__main__":
    unittest.main()
