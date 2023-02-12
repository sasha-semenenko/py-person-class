class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for human in people:
        result.append(Person(human["name"], human["age"]))

    for human in people:
        human_ = Person.people.get(human["name"])
        if human.get("wife"):
            human_.wife = Person.people[human["wife"]]
        if human.get("husband"):
            human_.husband = Person.people[human["husband"]]
    return result
