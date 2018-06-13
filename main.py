# Isaac Morrow, 2018
# Edit
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
        self.tags = ["crt", "crt", "pci", "wrk"]

    def select_event(self, event):
        for tag in event.tags:
            self.tags.append(tag)

    def get_tags(self):
        return self.tags

    def greatest(ls, amount):
        # self.amount = amount
        # self.ls = ls
        out = []
        for i in range(amount):
            self.highest = max(ls)
            out.append(self.highest)
            ls.remove(self.highest)
        print(self.out)
        return self.out

    def suggest(self, event_list, suggest_amount):
        self.suggest_amount = suggest_amount
        self.event_scores = []
        for event in event_list:
            print("Event: ", event.name)
            self.score = 0
            for event_tag in event.tags:
                for student_tag in self.tags:
                    if student_tag == event_tag:
                        self.score += 1
                    else:
                        pass
            event.score = self.score
            print(event.name, "score:", event.score)
            self.event_scores.append(event)



        # self.out = []
        # for i in range(self.suggest_amount):
        #     self.highest = max(self.event_scores)
        #     print(max(self.event_scores[i]))
        #     self.out.append(self.highest)
        #     ls.remove(self.highest)
        #     print()


hackerspace = MakeEvent("Hackerspace", "wrk", "ct", "lc")
at_issue = MakeEvent("At Issue", "crt", "pci", "par", "wrk", "lc")
events = [hackerspace, at_issue]

isaac = Student()
isaac.get_tags()
isaac.suggest(events, 3)
