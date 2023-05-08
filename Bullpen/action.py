class Action:
    # Check every 1s
    DEFAULT_REFRESH_RATE = 1

    def on_perform(self):
        raise NotImplementedError

    def refresh_rate(self):
        return self.DEFAULT_REFRESH_RATE

    def on_rotate_to(self):
        pass

    def on_rotate_from(self):
        pass

    def ready_to_rotate(self):
        return True
    
    def add_transitions(self, *transitions):
        for transition in transitions:
            self.transitions.append(transition)

    @property
    def transitions(self):
        if not hasattr(self, "_transitions"):
            self._transitions = []

        return self._transitions
