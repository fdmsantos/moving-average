from events.validations.RuleAbstract import RuleAbstract


class IsEquals(RuleAbstract):

    def handle_request(self):
        if self.event[self.field] != self.value:
            return False
        else:
            return self._successor.handle_request() if self._successor is not None else True
