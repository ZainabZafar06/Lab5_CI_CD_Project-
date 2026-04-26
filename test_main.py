import unittest
from main import add_student, update_marks, calculate_average, students

class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        students.clear()

    def test_add_student(self):
        add_student("Zainab", 80)
        self.assertEqual(len(students), 1)

    def test_update_marks(self):
        add_student("Zainab", 80)
        update_marks("Zainab", 90)
        self.assertEqual(students[0]["marks"], 90)

    def test_average(self):
        add_student("A", 50)
        add_student("B", 100)
        self.assertEqual(calculate_average(), 75)

    def test_empty_average(self):
        self.assertEqual(calculate_average(), 0)

    def test_invalid_update(self):
        update_marks("X", 50)
        self.assertEqual(len(students), 0)

if __name__ == "__main__":
    unittest.main()