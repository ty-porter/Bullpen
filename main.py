import Bullpen

import time
import sys


def fifty_fifty():
    import random

    return random.randint(0, 100) < 50


class MessageAction(Bullpen.Action):
    def __init__(self, message):
        self.message = message

    def on_perform(self):
        t = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
        sys.stdout.write(f"{self.message} @ {t}            \r")
        sys.stdout.flush()


main_action = MessageAction("Main Action")
secondary_action = MessageAction("Secondary Action")
tertiary_action = MessageAction("Tertiary Action")

main_action.add_transitions(
    Bullpen.Transition(to=secondary_action, on=Bullpen.Condition.Timer(2))
)
secondary_action.add_transitions(
    Bullpen.Transition(to=tertiary_action, on=Bullpen.Condition.Timer(3))
)
tertiary_action.add_transitions(
    Bullpen.Transition(to=main_action, on=Bullpen.Condition.Timer(4))
)

manager = Bullpen.Manager(entrypoint=main_action)

manager.perform()
