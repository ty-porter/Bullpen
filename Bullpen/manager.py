import time


class Manager:
    def __init__(self, entrypoint):
        self.current_action = self._entrypoint = entrypoint
        self._next_action = None
        
    def perform(self):
        self.reset_transition_conditions()

        self.current_action.on_rotate_to()

        while not (self.ready_to_rotate() and self.current_action.ready_to_rotate()):
            self.current_action.on_perform()

            time.sleep(self.current_action.refresh_rate())

        self.current_action.on_rotate_from()

        self.rotate()

    def rotate(self):
        self.current_action = self._next_action
        self._next_action = None

        self.perform()

    def ready_to_rotate(self):
        for transition in self.current_action.transitions:
            if transition.can_transition():
                self._next_action = transition.to

                return True

        return False

    def reset_transition_conditions(self):
        for transition in self.current_action.transitions:
            transition.on.reset_condition()
