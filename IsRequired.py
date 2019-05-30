from RuleAbstract import RuleAbstract


class IsRequired(RuleAbstract):

    def handle_request(self):
        if self.field not in self.event:
            return False
        else:
            return self._successor.handle_request() if self._successor is not None else True
