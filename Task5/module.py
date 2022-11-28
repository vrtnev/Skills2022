import unittest

def unique_elements(elements: list):
    setelements = set(elements)
    listelements = list(setelements)
    countelements = len(listelements)
    return countelements

class Person:
    def init(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def sort(persons: list, sort_by: str):
        result = sorted(persons, key=lambda x: getattr(x, attribute))
        return sorted_persons
        
class tests(unittest.TestCase):

    def test_unique_elements(self):
        self.assertEqual(unique_elements([1, 6, 2, 6]), 3)
        self.assertEqual(unique_elements([0, 6, 0, 0, 0]), 2)
        self.assertEqual(unique_elements([1, 1, 1, 1, 1]), 5)
        
    def test_sort(self):
        self.assertEqual(sort([p1, p2, p3], "firstname"), [p1, p3, p2])
        self.assertEqual(sort([p1, p2, p3], "lastname"), [p3, p2, p1])
        self.assertEqual(sort([p1, p2, p3], "age"), [p3, p1, p2])
        
p1 = Person("Nikolai", "Vorotnev", 16)
p3 = Person("Taylor", "Swift", 23)
p1 = Person("Somebody", "Else", 10)

