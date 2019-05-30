from src.events.validations.RuleAbstract import RuleAbstract


class IsEquals(RuleAbstract):

    def handle_request(self):
        if self.field in self.event:
            if self.event[self.field] != self.value:
                return False
        return self._successor.handle_request() if self._successor is not None else True
