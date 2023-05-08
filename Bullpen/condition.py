import time


class Condition:
    class _ConditionNode:
        def reset_condition(self):
            for cond in (self.cond1, self.cond2):
                if hasattr(cond, "reset_condition"):
                    cond.reset_condition()

    class _And(_ConditionNode):
        def __init__(self, cond1, cond2):
            self.cond1 = cond1
            self.cond2 = cond2

        def __call__(self):
            return self.cond1() and self.cond2()

    class _Or(_ConditionNode):
        def __init__(self, cond1, cond2):
            self.cond1 = cond1
            self.cond2 = cond2

        def __call__(self):
            return self.cond1() or self.cond2()

    def __init__(self, cond):
        self.condition = Condition._And(cond, Condition.Always)

    def AND(self, cond):
        self.condition = Condition._And(self.condition, cond)

        return self

    def OR(self, cond):
        self.condition = Condition._Or(self.condition, cond)

        return self

    @classmethod
    def Always(cls):
        return Condition(lambda: True)

    @classmethod
    def Never(cls):
        return Condition(lambda: False)

    def reset_condition(self):
        self.condition.reset_condition()

    def __call__(self):
        return self.condition()

    def Timer(amt):
        return _Timer(amt)


class _Timer(Condition):
    def __init__(self, amt):
        super().__init__(self)

        self.amt = amt
        self.reset_condition()

    def reset_condition(self):
        self.end_time = time.time() + self.amt

    def __call__(self):
        return time.time() >= self.end_time
