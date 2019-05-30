from RuleAbstract import RuleAbstract


class IsInteger(RuleAbstract):

    def handle_request(self):
        if not type(self.event[self.field]) == int:
            return False
        else:
            return self._successor.handle_request() if self._successor is not None else True
