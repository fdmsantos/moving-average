from src.events.validations.RuleAbstract import RuleAbstract


class IsInteger(RuleAbstract):

    def handle_request(self):
        if self.field in self.event:
            if not type(self.event[self.field]) == int:
                return False
        return self._successor.handle_request() if self._successor is not None else True
