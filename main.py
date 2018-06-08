# Isaac Morrow, 2018
# Suggests a flex event to a student using tags
from collections import Counter


class MakeEvent:
    """The teacher makes an event with a name and tags that relate to that
    flex event."""

    def __init__(self, name, *args):
        self.name = name
        self.tags = args


class Student:
    """Holds the students tags."""

    def __init__(self):
        self.tags = []

    def select_event(self, event):
        for tag in event.tags:
            self.tags.append(tag)

    def get_tags(self):
        return Counter(self.tags)

    def suggest(self, events):
        pass

hackerspace = MakeEvent("Hackerspace", "wrk", "ct", "lc")
at_issue = MakeEvent("At Issue", "crt", "pci", "par", "wrk", "lc")
events = [hackerspace, at_issue]

student = Student()
tags = student.get_tags()
print(list(tags.elements()))
