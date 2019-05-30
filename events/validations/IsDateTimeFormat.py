import datetime
from events.validations.RuleAbstract import RuleAbstract


class IsDateTimeFormat(RuleAbstract):

    def handle_request(self):
        if self.field in self.event:
            try:
                datetime.datetime.strptime(self.event[self.field], self.value)
            except ValueError:
                return False

        return self._successor.handle_request() if self._successor is not None else True
