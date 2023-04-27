class Transition:

    def __init__(self, **options):
        self.to = options["to"]
        self.on = options["on"]

    def can_transition(self):
        return self.on()
    
    def transition(self):
        if self.can_transition():
            return self.to
