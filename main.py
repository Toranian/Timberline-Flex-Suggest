# Isaac Morrow, 2018
# Suggests a flex event to a student using tags
from collections import Counter


class MakeEvent:
    """The teacher makes an event with a name and tags that relate to that
    flex event."""

    def __init__(self, name, *args):
        self.name = name
        self.tags = args
        self.score = 0


class Student:
    """Holds the students tags."""

    def __init__(self):
        self.tags = ["crt", "crt"]

    def select_event(self, event):
        for tag in event.tags:
            self.tags.append(tag)

    def get_tags(self):
        return self.tags

    def suggest(self, event_list, suggest_amount):
        self.suggest_amount = suggest_amount
        self.event_scores = []

        # Make the score for the flex events
        for event in event_list:
            self.score = 0
            for event_tag in event.tags:
                for student_tag in self.tags:
                    if student_tag == event_tag:
                        self.score += 1
                    else:
                        pass
            event.score = self.score
            self.event_scores.append(event)

        # Find the highest scoring events
        out = []
        for _ in range(self.suggest_amount):
            tmp = 0
            for i in self.event_scores:
                if i.score > tmp:
                    tmp = i.score
                else:
                    pass
            out.append(i.name)
            print(i.score)
            i.score = 0
        print(out)





hackerspace = MakeEvent("Hackerspace", "wrk", "ct", "lc")
at_issue = MakeEvent("At Issue", "crt", "pci", "par", "wrk", "lc", "crt")
events = [hackerspace, at_issue]

isaac = Student()
isaac.get_tags()
isaac.suggest(events, 2)
