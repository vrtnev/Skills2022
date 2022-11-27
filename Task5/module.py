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
        
        
