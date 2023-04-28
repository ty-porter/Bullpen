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
