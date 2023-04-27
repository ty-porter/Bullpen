import Bullpen

import time

class Manager:

    def __init__(self, config):
        self.config = Manager._convert_transitions_to_list(config)
        self.current_action = list(self.config.keys())[0]
        self.current_transitions = self.config[self.current_action]
        self._next_action = None

    def perform(self):
        self.reset_transition_conditions()

        while not self.ready_to_rotate():
            self.current_action.on_perform()

            time.sleep(0.05)

        return self.rotate()

    def rotate(self):
        self.current_action = self._next_action
        self.current_transitions = self.config[self.current_action]
        self._next_action = None

        return self.perform()

    def ready_to_rotate(self):
        for transition in self.current_transitions:
            if transition.can_transition():
                self._next_action = transition.to

                return True

        return False
    
    def reset_transition_conditions(self):
        for transition in self.current_transitions:
            transition.on.reset_condition()
    
    @staticmethod
    def _convert_transitions_to_list(config):
        converted = {}

        for key, value in config.items():
            if isinstance(value, Bullpen.Transition):
                converted[key] = [value]
            else:
                converted[key] = value

        return converted
